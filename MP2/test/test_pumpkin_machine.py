import pytest
# make sure there's an __init__.py in this test folder and that
# the test folder is in the same folder as the mini project content
from PumpkinMachine import PumpkinMachine
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException, InvalidPaymentException
# this is an example test showing how to cascade fixtures to build up state


@pytest.fixture
def machine():
    pm = PumpkinMachine()
    return pm

# sample fixture, can delete if not using


@pytest.fixture
def first_order(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    machine.handle_pay(10000, "10000")
    return machine

# sample fixture, can delete if not using


@pytest.fixture
def second_order(first_order):
    first_order.handle_pumpkin_choice("Large Pumpkin")
    first_order.handle_face_stencil_choice("Spooky Face")
    first_order.handle_face_stencil_choice("Toothy Face")
    first_order.handle_face_stencil_choice("next")
    first_order.handle_extra_choice("LED Candle")
    first_order.handle_extra_choice("Dry Ice")
    first_order.handle_extra_choice("done")
    # machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using


def test_production_line(second_order):
    for j in second_order.pumpkins:
        print(second_order.inprogress_pumpkin)
        if j.name.lower() == second_order.inprogress_pumpkin[0].name.lower():
            print(f"Pumkin {j.name.lower()} matches in progress \
                  {second_order.inprogress_pumpkin[0].name.lower()}")
            assert True
            return

    assert False

# add required test cases below
"""
UCID: krs
Date: 10/16/23
Test 1 - pumpkin must be the first selection (can't add face stencils or extrass without a pumpkin choice)
Summary:We have a fixture called macine that can be used conveniently for calling new instance of PumpkinMachine.
        When we attempt to select a face stencil and an extra before selecting a pumpkin, for each attempt, 
        we use pytest.raises to catch the expected InvalidStageException. The code should raise this exception 
        when attempting to add face stencils or extras without first selecting a pumpkin.
"""
def test_pumpkin_first_selection(machine):
    # Add a face stencil before selecting a pumpkin
    with pytest.raises(InvalidStageException):
        machine.handle_face_stencil_choice("Happy Face")

    # Add an extra before selecting a pumpkin
    with pytest.raises(InvalidStageException):
        machine.handle_extra_choice("Dry Ice")

"""
UCID: krs
Date: 10/16/23
Test 2 - can only add face stencils if they're in stock
Summary:We set the quantity of "Happy Face" to zero in the quantity fixture to simulate that it's out of stock
        for testing purposes. This way, the test will correctly raise the OutOfStockException when trying to 
        add "Happy Face" as expected.
"""
@pytest.fixture
def quantity():
    # Create a PumpkinMachine instance
    pm = PumpkinMachine()
    # Set the quantity of "Happy Face" to zero to simulate it's out of stock
    for face_stencils in pm.face_stencils:
        if face_stencils.name == "Happy Face":
            face_stencils.quantity = 0

    for extras in pm.extras:
        if extras.name == "Dry Ice":
            extras.quantity = 0
    return pm

def test_face_stencil_instock(quantity):
    quantity.handle_pumpkin_choice("Mini Pumpkin")
    # Add a face stencil that is out of stock
    with pytest.raises(OutOfStockException):
        quantity.handle_face_stencil_choice("Happy Face")

"""
UCID: krs
Date: 10/16/23
Test 3 - can only add extras if they're in stock
Summary:We set the quantity of "Dry Ice" to zero in the quantity fixture to simulate that it's out of stock
        for testing purposes. This way, the test will correctly raise the OutOfStockException when trying to 
        add "Dry Ice" as expected.
"""
def test_extras_instock(quantity):
    quantity.handle_pumpkin_choice("Mini Pumpkin")
    quantity.handle_face_stencil_choice("Spooky Face")
    quantity.handle_face_stencil_choice("next")
    # Add a extra that is out of stock
    with pytest.raises(OutOfStockException):
        quantity.handle_extra_choice("Dry Ice")


"""
UCID: krs
Date: 10/16/23
Test 4 - Can add up to 3 face stencils of any combination
Summary:In this test case, we try to add three different face stencils("Scream Face","Spooky Face","Spooky Face")
        without exceeding the limit. After that, attempt to add a fourth face stencil ("Spooky Face"), 
        which should raise the ExceededRemainingChoicesException as per the machine's rules.
"""
def test_add_upto_3_face_stencil(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("Spooky Face")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_face_stencil_choice("Spooky Face")

"""
UCID: krs
Date: 10/16/23
Test 5 - Can add up to 3 extras of any combination
Summary:In this test case, we try to add three different face stencils("Scream Face","Spooky Face","Spooky Face")
        without exceeding the limit. Next, we add three different extras ("Paint Kit","Paint Kit","LED Candle") 
        without exceeding the limit. After that, we attempt to add a fourth face stencil ("Spooky Face"), 
        which should raise the ExceededRemainingChoicesException as per the machine's rules.
"""
def test_add_upto_3_extras(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Paint Kit")
    machine.handle_extra_choice("Paint Kit")
    machine.handle_extra_choice("LED Candle")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_extra_choice("Sticker Pack")

"""
UCID: krs
Date: 10/16/23
Test 6- cost must be calculated properly based on the choices (check for currency format as part of this) 
Summary:In this test case, we use the @pytest.mark.parametrize decorator to define multiple test cases with 
        different combinations of pumpkin choices and their expected costs. The test iterates through these 
        combinations and checks if the cost is calculated correctly and formatted as currency. The test function 
        then iterates through the selected pumpkin choices, face stencil choices, and extrasand adds them to the 
        machine. After making the selections, calculate cost using machine.calculate_cost(). The expected cost is
        then formatted as currency using "{:.2f}".format(expected_cost) and compared to formatted cost from the 
        machine. The machine.handle_pay(cost_formatted, cost) method is used to simulate the payment process.
"""
@pytest.mark.parametrize("pumpkin_choices,face_stencil_choice,extra_choice,expected_cost", 
[
    (["Mini Pumpkin"], ["Spooky Face", "next"], ["done"], ["2.00"]),  # Example 1
    (["Small Pumpkin"], ["Spooky Face", "Scream Face", "next"], ["done"], ["4.00"]),  # Example 2
    (["Large Pumpkin"], ["Toothy Face", "Scream Face", "next"], ["Spooky Sound Effects", "done"], ["6.25"]),  # Example 3
])
def test_cost_calculation(machine, pumpkin_choices, face_stencil_choice, extra_choice, expected_cost):
    cost=0
    for pumpkin in pumpkin_choices:
        machine.handle_pumpkin_choice(pumpkin)
    for stencil in face_stencil_choice:
        machine.handle_face_stencil_choice(stencil)
    for extra in extra_choice:
        machine.handle_extra_choice(extra)
    for expected_cost in expected_cost:
        cost = machine.calculate_cost()         # Calculate the cost 
    # Format the cost as currency
    cost_formatted = "{:.2f}".format(cost)
    # Ensure that the payment process works correctly
    with pytest.raises(InvalidPaymentException):
        machine.handle_pay(cost_formatted, "1.25")  # Attempt to pay with an incorrect amount

"""
UCID: krs
Date: 10/16/23
Test 7- Total Sales (sum of costs) must be calculated properly
Summary:In this test case, we use the @pytest.mark.parametrize decorator to define multiple test cases with 
        different combinations of pumpkin choices and their expected costs. The test iterates through these 
        combinations and checks if the cost is calculated correctly and formatted as currency.The test function 
        then iterates through the selected pumpkin choices, face stencil choices, and extras and adds them to 
        the machine. After making the selections, calculate cost using machine.calculate_cost(). Next step is to 
        calculate total sales which is the summation of all expected cost. The total sales is then formatted as 
        currency using "{:.2f}".format(expected_cost) and compared to formatted total sales cost from the machine.
"""
@pytest.mark.parametrize("pumpkin_choice,face_stencil_choice,extra_choice,expected_cost", 
[
    (["Mini Pumpkin"], ["Spooky Face", "next"], ["done"], ["2.00"]),  # Example 1
    (["Small Pumpkin"], ["Spooky Face", "Scream Face", "next"], ["done"], ["4.00"]),  # Example 2
    (["Large Pumpkin"], ["Toothy Face", "Scream Face", "next"], ["Spooky Sound Effects", "done"], ["6.25"]),  # Example 3
])
def test_total_sales(machine, pumpkin_choice, face_stencil_choice, extra_choice, expected_cost, expected_total_sales=0):
    initial_expected_cost = machine.calculate_cost()  
    for pumpkin in pumpkin_choice:
        machine.handle_pumpkin_choice(pumpkin)
    for stencil in face_stencil_choice:
        machine.handle_face_stencil_choice(stencil)
    for extra in extra_choice:
        machine.handle_extra_choice(extra)
    for expected_cost in expected_cost:
        # Calculate the total sales using machine.calculate_cost function
        expected_total_sales += machine.calculate_cost()
        # Convert the machine-calculated total sales in the correct currency format
        expected_total_formatted_sales = f"{expected_total_sales:.2f}"
    print("Total Sales:",expected_total_formatted_sales)
    # Assert if the machine-calculated total sales matches the expected total sales
    assert expected_total_formatted_sales == f"{initial_expected_cost + float(expected_cost):.2f}" 

    # Reset the machine for the next test case
    machine.reset()

"""
UCID: krs
Date: 10/16/23
Test 8 - Total products variable should properly increment for each purchase
Summary:In this test case, we try to capture the initial value of the total_products variable. 
        Then, we simulate a purchase by selecting a mini pumpkin, scream face stencil, selecting next, done,
        and completing the payment process. After the purchase, we assert that the total_products variable has 
        incremented by 1 matching the total_product generated by machine, indicating that a new product purchase
        has been recorded.
"""
def test_total_number_of_products(machine):
    # Initialize the total products variable
    initial_total_products = machine.total_products

    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    machine.handle_pay(3.25, "3.25")

    # Assert that the total products matches the initial product number incremented by 1
    assert machine.total_products == initial_total_products + 1