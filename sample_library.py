# sample_library.py

class librarySystem:  # Issue: Class name doesn't follow CamelCase
    def __init__(self):
        self.Books = []  # Issue: Variable name should be lowercase
        self.MAXBOOKS = 1000  # Issue: Constant should be all uppercase with underscores
        self.available_status = None  # Issue: Potential null reference
    
    def ADD_BOOK(self, title, author):  # Issue: Method name should be lowercase
        """Add a new book to the library"""
        try:
            book = {
                "title": title,
                "author": author,
                "status": "available"
            }
            self.Books.append(book)  # Issue: Direct list manipulation
        except:  # Issue: Bare except clause
            print("Error adding book")  # Issue: Using print instead of logging
    
    def search_by_title(self, title, author_name, publisher, isbn, year, edition, category, language, format_type, pages, price):  # Issue: Too many parameters
        """
        Search for a book by title
        """
        # Issue: Complex nested loops and conditions
        found_books = []
        for book in self.Books:
            if book["title"].lower() == title.lower():
                if book["author"].lower() == author_name.lower():
                    if "publisher" in book and book["publisher"] == publisher:
                        if "isbn" in book and book["isbn"] == isbn:
                            if "year" in book and book["year"] == year:
                                if "edition" in book and book["edition"] == edition:
                                    found_books.append(book)
        
        return found_books

    def calculate_late_fees(self, days_overdue):  # Issue: Long method with multiple responsibilities
        """Calculate late fees for overdue books"""
        base_fee = 0.50
        max_fee = 50.00
        holiday_discount = 0.2
        weekend_discount = 0.1
        member_discount = 0.15
        senior_discount = 0.25
        student_discount = 0.3
        first_time_discount = 0.1
        loyalty_discount = 0.05
        seasonal_discount = 0.1
        bulk_discount = 0.1
        
        total_fee = days_overdue * base_fee
        
        if self.is_holiday():
            total_fee = total_fee - (total_fee * holiday_discount)
        if self.is_weekend():
            total_fee = total_fee - (total_fee * weekend_discount)
        if self.is_member():
            total_fee = total_fee - (total_fee * member_discount)
        if self.is_senior():
            total_fee = total_fee - (total_fee * senior_discount)
        if self.is_student():
            total_fee = total_fee - (total_fee * student_discount)
        if self.is_first_time():
            total_fee = total_fee - (total_fee * first_time_discount)
        if self.is_loyal_customer():
            total_fee = total_fee - (total_fee * loyalty_discount)
        if self.is_seasonal_promotion():
            total_fee = total_fee - (total_fee * seasonal_discount)
        if self.has_bulk_discount():
            total_fee = total_fee - (total_fee * bulk_discount)
            
        return min(total_fee, max_fee)
    
    def is_holiday(self): return True  # Issue: One-line methods without proper documentation
    def is_weekend(self): return True
    def is_member(self): return True
    def is_senior(self): return True
    def is_student(self): return True
    def is_first_time(self): return True
    def is_loyal_customer(self): return True
    def is_seasonal_promotion(self): return True
    def has_bulk_discount(self): return True

    def Process_Returns(self, bookId):  # Issue: Inconsistent method naming
        global_var = "This is bad practice"  # Issue: Using global variables
        
        try:
            book = None
            for b in self.Books:
                if b['id'] == bookId:
                    book = b
                    break
            
            if book == None:  # Issue: Using == None instead of is None
                return False
            
            book['status'] = 'available'
            return True
            
        except Exception as e:  # Issue: Catching generic Exception
            print(f"Error: {str(e)}")  # Issue: Using print for errors
            return False

    def get_all_books(self):  # Issue: Method potentially exposing internal state
        return self.Books  # Issue: Returning direct reference to internal list

# Issue: Duplicate code block
def calculate_fine(days, rate):
    total = 0
    for i in range(days):
        total += rate
    return total

def calculate_penalty(days, rate):  # Issue: Duplicate function with different name
    total = 0
    for i in range(days):
        total += rate
    return total

# Issue: Global variable
GLOBAL_LIBRARY = librarySystem()

if __name__ == "__main__":
    # Issue: Hard-coded values
    lib = librarySystem()
    lib.ADD_BOOK("Python Programming", "John Doe")
    lib.Process_Returns(123)
