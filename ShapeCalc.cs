using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeCalc
{
   // ShapeCalc - Written by Darryl Medley for TWiT Coding 101 on 9/16/2014

   // This is a simple demo of Object-Oriented Programming / Polymorphism
   // that shows how to use an abstract base class and sub-classes. 
   // I SWEAR I thought of this before seeing the MSDN examples that are very similar.

   // Declare a base "shape" class
   public abstract class Shape
   {  // Declare abstrct methods that the sub-classes must implement.
      public abstract void GetDimensions();
      public abstract double CalcArea();

      // A little utility method for user input used by the sub-classes
      public double GetFloat()
      {
         while (true) {
            string s = Console.ReadLine();
            try
            {
               return Convert.ToDouble(s);
            }
            catch
            {
               Console.Write("\nInvalid number. Please re-enter: ");
            }
         }
      }
   }

   // Declare sub-classes of Shape that do the real work
   public class Square : Shape
   {
      // A field to hold the user input. More complex shapes would have
      // multiple fields for the different sides.
      private double SideLen;  

      // override the base's abstract methods with real code
      public override void GetDimensions()
      {
         Console.Write("Enter the length of a side: ");
         SideLen = GetFloat();  // call our little utility method in the parent class
      }
      public override double CalcArea()
      {
         return SideLen * SideLen;
      }
   }

   public class Circle : Shape
   {
      private double radius;  // A field to hold the user input

      public override void GetDimensions()
      {
         Console.Write("Enter the length of the radius: ");
         radius = GetFloat();  // call our little utility method in the parent class
      }
      public override double CalcArea()
      {
         return radius * radius * Math.PI;
      }
   }

   // ***** Homework: Add more shape sub-classes here ****

   class Program
   {
      // This is the Main Menu function. It creates and returns a
      // sub-class of Shape based on the user's selection or null 
      // if nothing is selected.
      // NOTE: This is the only part of the main program's code 
      // that needs to be modified to add more shapes.
      // ALSO NOTE: This method is defined to return a type of 
      // "Shape" but it actually returns a sub-class of Shape. 
      // This is Polymorphism in action.
      static Shape GetShape()
      {
         string ShapeNbr = "x";
         while (true) {
            Console.WriteLine("\n1. Square");
            Console.WriteLine("2. Circle");
            Console.Write("Enter Shape Number: ");
            ShapeNbr = Console.ReadLine();
            if (ShapeNbr == "")  // Enter key alone pressed
               return null;  // return a null object reference
            else if (ShapeNbr == "1") 
               return new Square();  // Create and return a Shape sub-class
            else if (ShapeNbr == "2")
               return new Circle();  // Create and return a Shape sub-class 
         }
      }

      // This routine calls the methods defined in the base Shape class but
      // implemented in the sub-classes. Note that the parameter is type Shape
      // but we actually pass an object of the sub-class (Square, Circle, etc.)
      // This is the real power of Polymorphism. We can write code for the 
      // base class but at runtime it actually runs the code in the sub-class
      // that we pas to it.
      static void ProcessShape(Shape shp)
      {  // call the shape methods (implemented in the sub-class)
         shp.GetDimensions();
         double area = shp.CalcArea();
         Console.WriteLine("\nArea: {0:#,##0.###}", area);
      }

      static void Main(string[] args)
      {
         Console.WriteLine("Shape Area Calculator");
         while (true) {
            // Call the menu function that returns a shape object.
            // Note that it actually returns a sub-class object of shape
            // but we can store it in an object variable of the base class.
            Shape workShape = GetShape();  
            if (workShape != null) 
               // Pass the shape sub-class object to the processing function
               ProcessShape(workShape);
            else
               break;
         }
      }
   }
}
