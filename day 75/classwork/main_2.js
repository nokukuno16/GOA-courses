function BankAccount(owner, balance) {
    this.owner = owner; 
    this.balance = balance;
  
  
    this.deposit = function(amount) {
      if (amount > 0) {
        this.balance += amount;
        console.log(`${amount} ₾ დამატებულია. ახალი ბალანსი: ${this.balance} ₾`);
      } else {
        console.log("თანხა უნდა იყოს დადებითი რიცხვი.");
      }
    };
  
    
    this.withdraw = function(amount) {
      if (amount > 0 && amount <= this.balance) {
        this.balance -= amount;
        console.log(`${amount} ₾ გამოტანილია. დარჩენილი ბალანსი: ${this.balance} ₾`);
      } else if (amount > this.balance) {
        console.log("ბალანსზე საკმარისი თანხა არ არის.");
      } else {
        console.log("თანხა უნდა იყოს დადებითი რიცხვი.");
      }
    };
  
  
    this.showBalance = function() {
      console.log(`${this.owner}: ${this.balance} ₾`);
    };
  }
  
  
  const account1 = new BankAccount("გიორგი", 1000);
  const account2 = new BankAccount("ნინო", 500);
  const account3 = new BankAccount("ლაშა", 2000);
  
  account1.deposit(500); 
  account1.withdraw(300); 
  account1.showBalance(); 
  
  account2.deposit(200); 
  account2.withdraw(100); 
  account2.showBalance(); 
  
  account3.withdraw(2500); 
  account3.showBalance();