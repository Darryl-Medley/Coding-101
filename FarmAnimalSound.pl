#!/usr/bin/perl

# Simple Farm Animal Sounds program for kids
# The user enters the name of an animal, such as cat, and text of the animal's
# sound is displayed (meow).
# Written on 06/19/2014 by Darryl Medley for Coding 101 on the TWiT network

# Create a hash to associate animals with sounds using key => value notation
%AnimalSoundsHash = (
   "cat" => "Meow",
   "chicken" => "Cluck, Cluck",
   "cow" => "Moo",
   "dog" => "Ruff, Ruff",
   "goat" => "Burp!",
   "horse" => "Neigh",
   "mouse" => "Squeek, Squeek",
   "pig" => "Oink, Oink",
   "sheep" => "Baa, Baa");

print "\nEnter a farm animal, \"list\" to list animals, or enter nothing to exit\n";

# Main loop - do..until a blank animal name is entered
do {
   print "\nPlease enter a farm animal: ";

   # Get the animal name using chomp to remove the \n from the input
   chomp($animal = <STDIN>);

   # Test for a non-empty animal name.
   # "ne" is the Perl string operator for "not equal to"
   if ($animal ne "") {
      # Load a local variable (hence the "my" in front) with a lower-case copy
      # of the user input to use for case-insensitive comparisons
      my $testkey = lc $animal;

      # Check if the user wants to print a list of the animals
      if ($testkey eq "list") {
         print "\nAnimals on my farm:\n";

         # Loop through all entries in the hash using a foreach loop:
         # (keys %hash) lists each key. (values %hash) would list each value.
         foreach my $key (keys %AnimalSoundsHash) {
            print "$key\n";   # Print each animal name in our hash table
         }
      }
      else {
         # use the "exists" function to see if animal is in the hash
         if (exists($AnimalSoundsHash{$testkey})) {
            print "A $animal says \"$AnimalSoundsHash{$testkey}\"\n"; }
         else {
            print "Sorry, my farm does not have a $animal\n"; }
      }
   }
} until ($animal eq "");   # loop until just Enter is pressed

print "\nGoodbye. Please come back to my farm soon.";
