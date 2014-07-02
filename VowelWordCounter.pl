#!/usr/bin/perl

# VowelWordCounter.pl - Program that counts the number of words containing
# each vowel using two different methods
# Written on 06/27/2014 by Darryl Medley for Coding 101 on the TWiT network

# declare local variables (using "my") to hold the entered sentence and a regex
my ($sentence, $tempregex);

# declare a local variable (using "my") to hold the vowel counts
my ($acount, $ecount, $icount, $ocount, $ucount, $ycount, $vcount);

# Main loop - do..until just Enter is pressed
do {
   print "\nEnter a sentence: ";

   # Input the sentence into the local variable
   $sentence = <STDIN>;

   # Process the sentence if something was typed in
   if ($sentence ne "\n") {
      # Count Method 1 - Straight-line code for each vowel. Easier to understand.

      # set local vowel count variables to 0
      $acount = $ecount = $icount = $ocount = $ucount = $ycount = 0;

      # Count the words containing a particular vowel using this regular expression:
      #  \S* means 0 or more non-whitespace characters follow the vowel
      #  \s means a whitespace character (end of a word or of the string) must be found
      #  /g the "global" option means do the test for all words in the string and allows
      #  the expression to work properly with the "while" loop
      #  i - the "i" modifier at the end means do a case-insensitive search

      while ($sentence =~ /a\S*\s/gi)
         { $acount++; }   # increment counter for each word containing the vowel
      while ($sentence =~ /e\S*\s/gi)
         { $ecount++; }
      while ($sentence =~ /i\S*\s/gi)
         { $icount++; }
      while ($sentence =~ /o\S*\s/gi)
         { $ocount++; }
      while ($sentence =~ /u\S*\s/gi)
         { $ucount++; }
      while ($sentence =~ /y\S*\s/gi)
         { $ycount++; }

      print "Words counted using a hard-coded regex for each vowel:\n";
      print "Number of words containing \"a\": $acount\n";
      print "Number of words containing \"e\": $ecount\n";
      print "Number of words containing \"i\": $icount\n";
      print "Number of words containing \"o\": $ocount\n";
      print "Number of words containing \"u\": $ucount\n";
      print "Number of words containing \"y\": $ycount\n";


      # Count Method 2 - Use a loop for each vowel
      print "\nWords counted using a loop:\n";
      foreach my $ltr ('a','e','i','o','u','y') {
         $tempregex = $ltr.'\S*\s';   # put the regex in a string variable
         $vcount = 0;
         while ($sentence =~ m/$tempregex/gi)
            { $vcount++; }
         print "Number of words containing \"$ltr\": $vcount\n";
      }
   }   # end if ($sentence ne "\n")
} until ($sentence eq "\n");   # loop until just Enter is pressed

