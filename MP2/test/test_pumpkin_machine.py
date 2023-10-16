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

def test_pumpkin_first_selection(machine):
    # Add a face stencil before selecting a pumpkin
    with pytest.raises(InvalidStageException):
        machine.handle_face_stencil_choice("Happy Face")

    # Add an extra before selecting a pumpkin
    with pytest.raises(InvalidStageException):
        machine.handle_extra_choice("Dry Ice")

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

def test_extras_instock(quantity):
    quantity.handle_pumpkin_choice("Mini Pumpkin")
    quantity.handle_face_stencil_choice("Spooky Face")
    quantity.handle_face_stencil_choice("next")
    # Add a extra that is out of stock
    with pytest.raises(OutOfStockException):
        quantity.handle_extra_choice("Dry Ice")

def test_add_upto_3_face_stencil(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("Spooky Face")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_face_stencil_choice("Spooky Face")

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