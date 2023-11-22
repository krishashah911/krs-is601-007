from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB

import pycountry
organization = Blueprint('organization', __name__, url_prefix='/organization')

@organization.route("/search", methods=["GET"])
def search():
    rows = []
    has_error = False
    organization_id = request.args.get("organization_id")
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, donation count as donations for the organization
    # don't do SELECT * and replace the below "..." portion
    # UCID: krs
    # Date: 11/21/23
    allowed_columns = ["name", "city", "country", "state", "modified", "created"]
    query = """
        SELECT
            IS601_MP3_Organizations.name as name, 
            IS601_MP3_Organizations.address as address, 
            IS601_MP3_Organizations.city as city, 
            IS601_MP3_Organizations.country as country, 
            IS601_MP3_Organizations.state as state, 
            IS601_MP3_Organizations.zip as zip, 
            IS601_MP3_Organizations.website as website,
            (SELECT COUNT(*) FROM IS601_MP3_Donations WHERE IS601_MP3_Donations.organization_id = IS601_MP3_Organizations.id) as donations,
            IS601_MP3_Organizations.id
        FROM
            IS601_MP3_Organizations
        WHERE 1=1
    """
    args = {} # <--- add values to replace %s/%(named)s placeholders
    
    # TODO search-2 get name, country, state, column, order, limit request args
    # UCID: krs
    # Date: 11/21/23

    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)

    # TODO search-3 append a LIKE filter for name if provided
    # UCID: krs
    # Date: 11/21/23
    if name:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{name}%"
    
    # TODO search-4 append an equality filter for country if provided
    # UCID: krs
    # Date: 11/21/23
    if country:
        query += " AND country = %(country)s"
        args["country"] = country

    # TODO search-5 append an equality filter for state if provided
    # UCID: krs
    # Date: 11/21/23    
    if state:
        query += " AND state = %(state)s"
        args["state"] = state

    # TODO search-6 append sorting if column and order are provided and within the allows columns and allowed order asc,desc
    # UCID: krs
    # Date: 11/21/23 
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"

    # TODO search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    # UCID: krs
    # Date: 11/21/23 
    try:
        limit = int(limit)
        if 1 <= limit <= 100:
            query += " LIMIT %(limit)s"
            args["limit"] = limit
        else:
            flash("Limit must be between 1 and 100", "error")
    except ValueError:
        flash("Limit must be a number.", "danger")

    # except ValueError:
    #     flash("Limit must be a number between 1 and 100.", "danger")
    # limit = 10 # TODO change this per the above requirements
    
    # query += " LIMIT %(limit)s"
    # args["limit"] = limit
    #print("query",query)
    #print("args", args)

    try:
        result = DB.selectAll(query, args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
        else:
            flash("Error retrieving organization records. Please try again later.", "error")
    except Exception as e:
        # TODO search-9 make message user friendly
        # UCID: krs
        # Date: 11/21/23 
        flash("An error occurred while retrieving organizations. Please try again later.", "danger")
    
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    
    # do this prior to passing to render_template, but not before otherwise it can break validation

    return render_template("list_organizations.html", rows=rows, allowed_columns=allowed_columns)


@organization.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        has_error = False # use this to control whether or not an insert occurs
        
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website, description
        # UCID: krs
        # Date: 11/21/23
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zip_code = request.form.get("zip")
        website = request.form.get("website","")
        description = request.form.get("description","")
        
        # TODO add-2 name is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not name:
            has_error = True
            flash("Organization Name is required", "danger")
        
        # TODO add-3 address is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not address:
            has_error = True
            flash("Address is required", "danger")

        # TODO add-4 city is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not city:
            has_error = True
            flash("Name of the city is required", "danger")
        state1 = country + "-" + state

        # TODO add-5 state is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not state:
            has_error = True
            flash("Name of the state is required", "danger")

        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation to solve this
        elif state1 not in [s.code for s in pycountry.subdivisions.get(country_code=country) ]:
            flash("Invalid State", "danger")
            has_error = True

        # TODO add-6 country is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not country:
            has_error = True
            flash("Name of the country is required", "danger")

        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation to solve this
        elif country not in [c.alpha_2 for c in pycountry.countries]:
            flash("Invalid Country", "danger")
            has_error = True

        # TODO add-7 website is not required
        # TODO add-8 zip is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # UCID: krs
        # Date: 11/21/23
        if not zip_code:
            has_error = True
            flash("Zip is required", "danger")

        # TODO add-9 description is not required

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Organizations
                (name, address, city, state, country, zip, website, description)
                    VALUES (%(name)s, %(address)s, %(city)s, %(state)s, %(country)s, 
                            %(zip)s, %(website)s, %(description)s)
                """, {
                    "name": name,
                    "address": address,
                    "city": city,
                    "state": state,
                    "country": country,
                    "zip": zip_code,
                    "website": website,
                    "description": description
                }
                ) # <-- TODO add-10 add query and add arguments
                # UCID: krs
                # Date: 11/21/23

                if result.status:
                    flash("Added Organization", "success")
            except Exception as e:
                # TODO add-11 make message user friendly
                # UCID: krs
                # Date: 11/21/23
                flash("An error occured while adding organization. Please try again later.", "danger")
        
    return render_template("manage_organization.html", org=request.form)

@organization.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("Organization ID is required", "danger")
        return redirect(url_for("organization.search"))

    if request.method == "POST":
        data = {"id": id} # use this as needed, can convert to tuple if necessary
        # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
        # UCID: krs
        # Date: 11/21/23
        name = request.form.get("name")
        description = request.form.get("description")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zip_code = request.form.get("zip")
        website = request.form.get("website")

        # TODO edit-3 name is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not name:
            flash("Organization Name is required", "danger")
            has_error = True
            return redirect(url_for("organization.edit", id=id))

        # TODO edit-4 address is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not address:
            flash("Address is required", "danger")
            has_error = True
            return redirect(url_for("organization.edit", id=id))
        # TODO edit-5 city is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not city:
            flash("Name of the city is required", "danger")
            has_error = True
            return redirect(url_for("organization.edit", id=id))
        # TODO edit-6 state is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not state:
            flash("Name of the state is required", "danger")
            has_error = True
            return redirect(url_for("organization.edit", id=id))
            
        # TODO edit-6a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        valid_states = [subdivision.code.split("-")[1] for subdivision in pycountry.subdivisions.get(country_code=country, default=[])]
        if state not in valid_states:
            flash("Invalid state selected.", "danger")
            return redirect(url_for("organization.edit", id=id))

        # TODO edit-7 country is required (flash proper error message)
        # UCID: krs
        # Date: 11/21/23
        if not country:
            flash("Name of the country is required", "danger")
            has_error = True
            return redirect(url_for("organization.edit", id=id))
            
        # TODO edit-7a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        valid_countries = [country.alpha_2 for country in pycountry.countries]
        if country not in valid_countries:
            flash("Invalid country selected.", "danger")
            return redirect(url_for("organization.edit", id=id))
            
        # TODO edit-8 website is not required
        # TODO edit-9 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # populate data dict with mappings
        # UCID: krs
        # Date: 11/21/23
        if not zip_code:
            flash("Zip code is required", "danger")
            has_error = True
            return redirect(url_for("organization.edit", id=id))
            
        data.update({
        "name": name,
        "description": description,
        "address": address,
        "city": city,
        "state": state,
        "country": country,
        "zip": zip_code,
        "website": website
    })
        has_error = False # use this to control whether or not an insert occurs

        if not has_error:
            try:
                # TODO edit-10 fill in proper update query
                # name, address, city, state, country, zip, website
                # UCID: krs
                # Date: 11/21/23
                result = DB.update("""
                UPDATE IS601_MP3_Organizations
                SET
                name = %(name)s,
                address = %(address)s,
                city = %(city)s,
                state = %(state)s,
                country = %(country)s,
                zip = %(zip)s,
                website = %(website)s,
                description = %(description)s
                WHERE 
                id = %(id)s
                """,data)
                    
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-11 make this user-friendly
                # UCID: krs
                # Date: 11/21/23
                print(f"{e}")
                flash("An error occurred while updating the record. Please try again later.", "danger")
    row = {}
    try:
        # TODO edit-12 fetch the updated data
        # UCID: krs
        # Date: 11/21/23
        result = DB.selectOne("""
        SELECT id, name, address, city, state, country, zip, website, description, created, modified
        FROM IS601_MP3_Organizations 
        WHERE IS601_MP3_Organizations.id = %(id)s
        """, {"id": id})
        if result.status:
            row = result.row
                
    except Exception as e:
        # TODO edit-13 make this user-friendly
        # UCID: krs
        # Date: 11/21/23
        flash("An error occurred while fetching the updated data. Please try again later.", "danger")
    
    return render_template("manage_organization.html", org=row)

@organization.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    # UCID: krs
    # Date: 11/21/23
    id = request.args.get("id")
    if not id:
        flash("Organization ID is required", "danger")
        return redirect(url_for("organization.search"))

    # TODO delete-2 delete organization by id (note: you'll likely need to trigger a delete of all donations related to this organization first due to foreign key constraints)
    # TODO delete-3 ensure a flash message shows for successful delete
    # TODO delete-4 pass all argument except id to this route
    # UCID: krs
    # Date: 11/21/23
    try:
        result = DB.delete("DELETE FROM IS601_MP3_Organizations WHERE id = %s", id)
        if result.status:
            flash("Record deleted", "success")
        else:
            flash("An error occurred while deleting the record. Please try again.", "danger")
    except Exception as e:
        flash(f"Delete error: {e}", "danger")

    # TODO delete-5 redirect to organization search
    # UCID: krs
    # Date: 11/21/23
    return redirect(url_for("organization.search"))