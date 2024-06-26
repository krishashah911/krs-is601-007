from enum import Enum
import sys
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from PumpkinMachineExceptions import InvalidPaymentException


class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity=10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity

    def in_stock(self):
        return self.quantity > 0

    def __repr__(self) -> str:
        return self.name


class Pumpkin(Usable):
    pass


class FaceStencil(Usable):
    pass


class Extra(Usable):
    pass


class STAGE(Enum):
    Pumpkin = 1
    FaceStencil = 2
    Extra = 3
    Pay = 4


class PumpkinMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 15
    MAX_STENCILS = 3
    MAX_EXTRAS = 3

    pumpkins = [Pumpkin(name="Mini Pumpkin", cost=1),
                Pumpkin(name="Small Pumpkin", cost=2),
                Pumpkin(name="Medium Pumpkin", cost=2.5),
                Pumpkin(name="Large Pumpkin", cost=3)]
    face_stencils = [FaceStencil(name="Happy Face", quantity=10, cost=1),
                     FaceStencil(name="Scream Face", quantity=10, cost=1),
                     FaceStencil(name="Toothy Face", quantity=10, cost=1),
                     FaceStencil(name="Spooky Face", quantity=10, cost=1)]
    extras = [Extra(name="Small Candle", quantity=10, cost=.25),
              Extra(name="LED Candle", quantity=10, cost=.25),
              Extra(name="Spooky Sound Effects", quantity=10, cost=1.25),
              Extra(name="Sticker Pack", quantity=10, cost=1.00),
              Extra(name="Paint Kit", quantity=10, cost=3),
              Extra(name="Dry Ice", quantity=10, cost=.25),
              Extra(name="Googly Eyes", quantity=10, cost=.25),
              Extra(name="Glitter", quantity=10, cost=.25)]

    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_stencils = MAX_STENCILS
    remaining_extras = MAX_EXTRAS
    total_sales = 0
    total_products = 0

    inprogress_pumpkin = []
    currently_selecting = STAGE.Pumpkin

    # rules
    # 1 - pumpkin must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - face stencils can't exceed max
    # 4 - extras can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more things can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_products should increment properly after a payment

    def pick_pumpkin(self, choice):
        if self.currently_selecting != STAGE.Pumpkin:
            raise InvalidStageException
        for c in self.pumpkins:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_pumpkin.append(c)
                return
        raise InvalidChoiceException

    def pick_face_stencil(self, choice):
        if self.currently_selecting != STAGE.FaceStencil:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_stencils <= 0:
            raise ExceededRemainingChoicesException
        for f in self.face_stencils:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_pumpkin.append(f)
                self.remaining_stencils -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_extras(self, choice):
        if self.currently_selecting != STAGE.Extra:
            raise InvalidStageException
        if self.remaining_extras <= 0:
            raise ExceededRemainingChoicesException
        for t in self.extras:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_pumpkin.append(t)
                self.remaining_extras -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        """Called when a pumpkin is complete"""
        self.remaining_stencils = self.MAX_STENCILS
        self.remaining_extras = self.MAX_EXTRAS
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING

    def handle_pumpkin_choice(self, _pumpkin):
        self.pick_pumpkin(_pumpkin)
        self.currently_selecting = STAGE.FaceStencil

    def handle_face_stencil_choice(self, _face_stencil):
        if _face_stencil == "next":
            self.currently_selecting = STAGE.Extra
        else:
            self.pick_face_stencil(_face_stencil)

    def handle_extra_choice(self, _extra):
        if _extra == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_extras(_extra)

# UCID: krs
# Date: 10/14/23
# Summary:For the handle_pay function, the expected cost of the current order is added only if it 
#         passes the payment process. And the toal is printed in total_sales variable.

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == str(expected):
            print("Thank you! Enjoy your Pumpkin and Happy Hallowween!")
            self.total_products += 1
            self.total_sales += expected 
            self.total_sales_formatted = "{:.2f}".format(self.total_sales)
            print(f"Total sales so far is ${self.total_sales_formatted}")
            self.reset()
        else:
            raise InvalidPaymentException

    def print_current_pumpkin(self):
        print(
            f"Current Pumpkin: {','.join([x.name for x in self.inprogress_pumpkin])}")


# UCID: krs
# Date: 10/14/23
# Summary:For the calculate_cost function, we try to run a for loop that adds costs of the selected 
#         pumpkin, face stencil, and extras in the inprogress_pimpkin list.

    def calculate_cost(self):
        cost = sum(item.cost for item in self.inprogress_pumpkin)
        return cost

    def run(self):
        try:
            if self.currently_selecting == STAGE.Pumpkin:
                pumpkin = input(
                    f"What type of pumpkin would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.pumpkins))))}?\n")
                self.handle_pumpkin_choice(pumpkin)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.FaceStencil:
                stencil = input(
                    f"Which type of face stencil would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.face_stencils))))}? Or type next.\n")
                self.handle_face_stencil_choice(stencil)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Extra:
                extra = input(
                    f"What extras would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.extras))))}? Or type done.\n")
                self.handle_extra_choice(extra)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()                # UCID: krs         Date: 10/14/23
                expected_formatted = "{:.2f}".format(expected)  # Show expected value as currency format
                total = input(                                  # Require total to be entered as currency format
                    f"Your total is ${expected_formatted}, please enter the exact value.\n")
                self.handle_pay(expected, total)

                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    # exit() in recursive functions creates stackoverflow
                    # use return 1 to exit
                    print("Quitting the pumpkin machine")
                    return 1
                
        except KeyboardInterrupt:
            # quit
            print("Quitting the pumpkin machine")
            sys.exit()

        # UCID: krs         Date: 10/14/23
        except OutOfStockException:
            if self.currently_selecting == STAGE.Pumpkin:
                category_name = "Pumpkin"
            elif self.currently_selecting == STAGE.FaceStencil:
                category_name = "Face Stencil"
            elif self.currently_selecting == STAGE.Extra:
                category_name = "Extra"
            # show an appropriate message of what stage/category was out of stock
            print(f"Bad news! Selected {category_name} is out of stock. Please choose another option.")

        # UCID: krs         Date: 10/14/23    
        except NeedsCleaningException:
            # prompt user to type "clean" to trigger clean_machine() any other input is ignored
            cleaning = input("The machine needs cleaning. Type 'clean' to proceed or any other input to ignore.\n")
            if cleaning.lower() == "clean":
                # Trigger the clean_machine method
                self.clean_machine()   
                # print a message whether or not the machine was cleaned                 
                print("The machine was cleaned. Thank you for your patience")
            else:
                print("Cleaning was not initiated. Please try again later")

        # UCID: krs         Date: 10/14/23
        except InvalidChoiceException:
            if self.currently_selecting == STAGE.Pumpkin:
                category_name = "Pumpkin"
            elif self.currently_selecting == STAGE.FaceStencil:
                category_name = "Face Stencil"
            elif self.currently_selecting == STAGE.Extra:
                category_name = "Extra"
            elif self.currently_selecting == STAGE.Pay:
                category_name = "Payment"
            # show an appropriate message of what stage/category was the invalid choice was in
            print(f"Invalid {category_name}. Please choose a valid {category_name}.")

        # UCID: krs         Date: 10/14/23    
        except ExceededRemainingChoicesException:
            if self.currently_selecting == STAGE.FaceStencil:
                category_name = "Face Stencils"
            elif self.currently_selecting == STAGE.Extra:
                category_name = "Extras"
            # show an appropriate message of which stage/category was exceeded
            print(f"Oops! You have exceeded the limit of {category_name} choice. Please proceed to the next step.")
            # move to the next stage/category
            if self.currently_selecting == STAGE.FaceStencil:
                self.currently_selecting = STAGE.Extra
            elif self.currently_selecting == STAGE.Extra:
                self.currently_selecting = STAGE.Pay
            else:
                self.currently_selecting = STAGE.Pumpkin 

        # UCID: krs         Date: 10/14/23 
        except InvalidPaymentException:
            # show an appropriate message
            print("Invalid Payment. Please enter the correct amount.")

        except Exception as e:
            # this is a default catch all, follow the steps above
            print(f"Something went wrong and I didn't handle it: {e}")

        self.run()

    def start(self):
        self.run()


if __name__ == "__main__":
    pm = PumpkinMachine()
    pm.start()