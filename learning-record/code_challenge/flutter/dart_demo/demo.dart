void main() {
  // Example of variables and string interpolation
  String name = 'Alice';
  int age = 25;
  print('Hello, my name is $name and I am $age years old');

  // Example of lists
  List<String> fruits = ['apple', 'banana', 'orange'];
  fruits.forEach((fruit) => print('I like $fruit'));

  // Example of a simple function
  int addNumbers(int a, int b) {
    return a + b;
  }

  // Using the function
  int result = addNumbers(5, 3);
  print('5 + 3 = $result');

  // Example of a class
  Person person = Person('Bob', 30);
  person.introduce();
}

class Person {
  String name;
  int age;

  Person(this.name, this.age);

  void introduce() {
    print('Hi, I am $name and I am $age years old');
  }
}