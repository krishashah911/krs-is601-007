import datetime
from datetime import timedelta
import re
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
donations = Blueprint('donations', __name__, url_prefix='/donations')

def is_valid_email(email):
    # A basic regex pattern for email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


@donations.route("/search", methods=["GET"])
def search():
    rows = []
    organization_name = ""
    has_error = False
    # DO NOT DELETE PROVIDED COMMENTS

    # TODO search-1 retrieve donation id as id, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments, organization_name using a LEFT JOIN
    # UCID: krs
    # Date: 11/21/23
    query = """
        SELECT
            d.id as 'id',
            d.donor_firstname as 'Donor Firstname',
            d.donor_lastname as 'Donor Lastname',
            d.donor_email as 'Donor Email',
            d.item_name as 'Item Name',
            d.item_description as 'Item Description',
            d.item_quantity as 'Item Quantity',
            d.donation_date as 'Donation Date',
            d.comments as Comments,
            o.name AS organization_name,
            d.created as created,
            d.modified as modified
        FROM
            IS601_MP3_Donations d
        LEFT JOIN
            IS601_MP3_Organizations o ON d.organization_id = o.id
        WHERE 1=1
    """
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["donor_firstname", "donor_lastname", "donor_email", "organization_name" ,"item_name", "item_quantity", "created", "modified"]
    
    # TODO search-2 get fn, ln, email, organization_id, column, order, limit from request args
    # UCID: krs
    # Date: 11/21/23
    d_id = request.args.get("id")
    fn = request.args.get("fn")
    ln = request.args.get("ln")
    email = request.args.get("email")
    item_name = request.args.get("item_name")
    organization_id = request.args.get("organization_id")
    column = request.args.get("column")  
    order = request.args.get("order")  
    limit = request.args.get("limit", 10) 
    
    # TODO search-3 append like filter for donor_firstname if provided
    # UCID: krs
    # Date: 11/21/23
    if fn:
        query += " AND d.donor_firstname LIKE %(donor_firstname)s"
        args["donor_firstname"] = f"%{fn}%"

    # TODO search-4 append like filter for donor_lastname if provided
    # UCID: krs
    # Date: 11/21/23
    if ln:
        query += " AND d.donor_lastname LIKE %(donor_lastname)s"
        args["donor_lastname"] = f"%{ln}%"

    # TODO search-5 append like filter for donor_email if provided
    # UCID: krs
    # Date: 11/21/23
    if email:
        query += " AND d.donor_email LIKE %(donor_email)s"
        args["donor_email"] = f"%{email}%"

    # TODO search-6 append like filter for item_name if provided
    # UCID: krs
    # Date: 11/21/23    
    if item_name:
        query += " AND d.item_name LIKE %(item_name)s"
        args["item_name"] = f"%{item_name}%"

    # TODO search-7 append equality filter for organization_id if provided
    # UCID: krs
    # Date: 11/21/23
    if organization_id:
        query += " AND d.organization_id = %(organization_id)s"
        args["organization_id"] = organization_id

    # TODO search-8 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # UCID: krs
    # Date: 11/21/23
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"

    # TODO search-9 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-10 provide a proper error message if limit isn't a number or if it's out of bounds
    # UCID: krs
    # Date: 11/21/23
    try:
        if limit:
            limit = int(limit)
            if 1 <= limit <= 100:
                query += " LIMIT %(limit)s"
                args["limit"] = limit
            else:
                flash("Limit must be between 1 and 100", "error")
    except ValueError:
        flash("Invalid limit value", "error")
        has_error = True
    
    print("query",query)
    print("args", args)

    if not has_error:
        try:
            result = DB.selectAll(query, args)
            if result.status:
                rows = result.rows
                # print(f"rows: {rows}")
            else:
                flash("Error retrieving donation records. Please try again.", "error")
        except Exception as e:
            # TODO search-11 make message user friendly
            # UCID: krs
            # Date: 11/21/23
            flash("An unexpected error occured. Please try again later.", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    # TODO search-12 if request args has organization identifier set organization_name variable to the correct name
    # UCID: krs
    # Date: 11/21/23

    if organization_id:
        try:
            result = DB.selectOne("SELECT name FROM IS601_MP3_Organizations WHERE id = %s", organization_id)
            if result.status:
                organization_id = result.row.get("id")
                organization_name = result.row.get("name")
            else:
                # TODO search-13 make this user-friendly
                # UCID: krs
                # Date: 11/21/23
                flash("An error occurred while fetching organization name. Please try again later.", "error")
        except Exception as e:
            # TODO search-14 make this user-friendly
            # UCID: krs
            # Date: 11/21/23
            print(f"organization name fetch error {e}")
            flash("An error occurred while fetching organization name. Please try again later.", "danger")
    else:
        organization_name = ""  

    return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns)
    
    # allowed_columns_tuples = [(col, col.replace("_", " ").capitalize()) for col in allowed_columns]
    # return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns_tuples)


@donations.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
        # UCID: krs
        # Date: 11/21/23
        donor_firstname = request.form.get("donor_firstname")
        donor_lastname = request.form.get("donor_lastname")
        donor_email = request.form.get("donor_email")
        organization_id = request.form.get("organization_id")
        item_name = request.form.get("item_name")
        item_description = request.form.get("item_description", "")
        item_quantity = request.form.get("item_quantity")
        donation_date = request.form.get("donation_date")
        comments = request.form.get("comments","")
        
        has_error = False
        
        # TODO add-2 donor_firstname is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not donor_firstname:
            has_error = True
            flash("Donor First Name is required", "danger")
        
        # TODO add-3 donor_lastname is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23        
        if not donor_lastname:
            has_error = True
            flash("Donor Last Name is required", "danger")
        
        # TODO add-4 donor_email is required (flash proper error message)
        # TODO add-4a email must be in proper format (flash proper message)
        # UCID: krs
        # Date: 11/21/23
        if not donor_email:
            has_error = True
            flash("Donor Email is required", "danger")
        else:
            if not is_valid_email(donor_email):
                has_error = True
                flash("Invalid email format", "error")

        # TODO add-5 organization_id is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not organization_id:
            has_error = True
            flash("Organization is required", "danger")
        
        # TODO add-6 item_name is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not item_name:
            has_error = True
            flash("Item Name is required", "danger")
        
        # TODO add-7 item_description is optional
        # TODO add-8 item_quantity is required and must be more than 0 (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not item_quantity or not item_quantity.isdigit() or int(item_quantity)  <= 0:
            has_error = True
            flash("Item Quantity must be greater than 0", "danger")
        
        # TODO add-9 donation_date is required and must be within the past 30 days
        # UCID: krs
        # Date: 11/21/23
        if not donation_date:
            has_error = True
            flash("Invalid donation date", "danger")
        else:
            try:
                donation_date = datetime.datetime.strptime(donation_date, "%Y-%m-%d") 
                if (datetime.datetime.now() - donation_date).days >30:
                    has_error = True
                    flash("Donation date must be within past 30 days", "danger")
            except ValueError:
                has_error = True
                flash("Invalid date format. Please use YYYY-MM-DD", "danger")   
        # TODO add-10 comments are optional

        if not has_error:
            try:
                result = DB.insertOne("""
                    INSERT INTO IS601_MP3_Donations (donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments)
                    VALUES (%(donor_firstname)s, %(donor_lastname)s, %(donor_email)s, %(organization_id)s, %(item_name)s, 
                            %(item_description)s, %(item_quantity)s, %(donation_date)s, %(comments)s)
                """, {
                    "donor_firstname": donor_firstname,
                    "donor_lastname": donor_lastname,
                    "donor_email": donor_email,
                    "organization_id": organization_id,
                    "item_name": item_name,
                    "item_description": item_description,
                    "item_quantity": item_quantity,
                    "donation_date": donation_date,
                    "comments": comments
                }
                ) # <-- TODO add-11 add query and add arguments
                # UCID: krs
                # Date: 11/21/23

                if result.status:
                    print("donation record created")
                    flash("Created Donation Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                # UCID: krs
                # Date: 11/21/23
                print(f"insert error {e}")
                flash("An error occured while creating donation record. Please try again later.", "danger")
    return render_template("manage_donation.html",donation=request.form)

@donations.route("/edit", methods=["GET", "POST"])
def edit():
    row = {}
    
    # TODO edit-1 request args id is required (flash proper error message)
    # UCID: krs
    # Date: 11/21/23
    donation_id = request.args.get("id")
    if not donation_id: # TODO update this for TODO edit-1
        flash("Donation ID is required", "danger")
        return redirect(url_for("donations.search"))
    else:
        if request.method == "POST":
            
            # TODO add-2 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            # UCID: krs
            # Date: 11/21/23
            donor_firstname = request.form.get("donor_firstname")
            donor_lastname = request.form.get("donor_lastname")
            donor_email = request.form.get("donor_email")
            organization_id = request.form.get("organization_id")
            item_name = request.form.get("item_name")
            item_description = request.form.get("item_description", "")
            item_quantity = request.form.get("item_quantity")
            donation_date = request.form.get("donation_date")
            comments = request.form.get("comments", "")
            
            # TODO add-3 donor_firstname is required (flash proper error message)
            # UCID: krs
            # Date: 11/21/23
            if not donor_firstname:
                flash("Donor First Name is required", "danger")
                has_error = True

            # TODO add-4 donor_lastname is required (flash proper error message)
            # UCID: krs
            # Date: 11/21/23
            if not donor_lastname:
                flash("Donor Last Name is required", "danger")
                has_error = True

            # TODO add-5 donor_email is required (flash proper error message)
            # UCID: krs
            # Date: 11/21/23
            if not donor_email:
                flash("Donor Email is required", "danger")
                has_error = True

            # TODO add-5a email must be in proper format (flash proper message)
            # UCID: krs
            # Date: 11/21/23
            elif not is_valid_email(donor_email):  # You need to implement validate_email function
                flash("Email must be in a proper format", "danger")
                has_error = True

            # TODO add-6 organization_id is required (flash proper error message)
            # UCID: krs
            # Date: 11/21/23
            if not organization_id:
                flash("Organization ID is required", "danger")
                has_error = True

            # TODO add-7 item_name is required (flash proper error message)
            # UCID: krs
            # Date: 11/21/23
            if not item_name:
                flash("Item Name is required", "danger")
                has_error = True

            # TODO add-8 item_description is optional
            # TODO add-9 item_quantity is required and must be more than 0 (flash proper error message)
            # UCID: krs
            # Date: 11/21/23
            if not item_quantity or int(item_quantity) <= 0:
                flash("Item Quantity must be greater than 0", "danger")
                has_error = True

            # TODO add-10 donation_date is required and must be within the past 30 days
            # UCID: krs
            # Date: 11/21/23
            try:
                donation_date = datetime.datetime.strptime(donation_date, "%Y-%m-%d")
                thirty_days_ago = datetime.datetime.now() - timedelta(days=30)
                if donation_date < thirty_days_ago:
                    flash("Donation Date must be within the past 30 days", "danger")
                    has_error = True
            except ValueError:
                flash("Invalid Date Format", "danger")
                has_error = True

            # TODO add-11 comments are optional
            has_error = False # use this to control whether or not an insert occurs
                
            if not has_error:
                try:
                    # TODO edit-12 fill in proper update query
                    # UCID: krs
                    # Date: 11/21/23
                    result = DB.update("""
                    UPDATE IS601_MP3_Donations SET
                    donor_firstname = %s,
                    donor_lastname = %s,
                    donor_email = %s,
                    organization_id = %s,
                    item_name = %s,
                    item_description = %s,
                    item_quantity = %s,
                    donation_date = %s,
                    comments = %s
                    WHERE id = %s
                    """, donor_firstname, donor_lastname, donor_email, organization_id, item_name,
                        item_description, item_quantity, donation_date, comments, donation_id,)
                    
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-13 make this user-friendly
                    # UCID: krs
                    # Date: 11/21/23
                    print(f"update error {e}")
                    flash("An error occurred while updating the record. Please try again later.", "danger")
        
        try:
            # TODO edit-14 fetch the updated data 
            # UCID: krs
            # Date: 11/21/23
            result = DB.selectOne("""
            SELECT IS601_MP3_Donations.id, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            FROM IS601_MP3_Donations 
            LEFT JOIN 
            IS601_MP3_Organizations ON IS601_MP3_Donations.organization_id = IS601_MP3_Organizations.id
            WHERE IS601_MP3_Donations.id = %s
            """
            , donation_id)
            
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-15 make this user-friendly
            # UCID: krs
            # Date: 11/21/23
            flash("An error occurred while fetching the updated data. Please try again later.", "danger")
    
    return render_template("manage_donation.html", donation=row)

@donations.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    # UCID: krs
    # Date: 11/21/23
    donation_id = request.args.get("id")
    if not donation_id:
        flash("Donation ID is required", "danger")
        return redirect(url_for("donations.search"))

    # TODO delete-2 delete donation by id (fetch the id from the request)
    # TODO delete-3 ensure a flash message shows for successful delete
    # TODO delete-4 pass all argument except id to this route
    # UCID: krs
    # Date: 11/21/23
    try:
        result = DB.delete("DELETE FROM IS601_MP3_Donations WHERE id = %s", donation_id)
        if result.status:
            flash("Record deleted", "success")
        else:
            flash("An error occurred while deleting the record. Please try again.", "danger")
    except Exception as e:
        flash(f"Delete error: {e}", "danger")

    # TODO delete-5 redirect to donation search
    # UCID: krs
    # Date: 11/21/23
    return redirect(url_for("donations.search"))
