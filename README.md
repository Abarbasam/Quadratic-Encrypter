# Quadratic-Encrypter
This is a simple encrypter/decrypter that takes a character's ASCII value, and applies it (as x) to a quadratic equation. All of the new number values are then strung together to create a very large looking number. See below for an in-depth explanation

# How the decryption script works
Here is an example of the encrypted version of, "Hello, World!"

```
1311240515664530744535140535140537114458924314452283453711453914253514053014043340
```

The decryption script does three things to get the *a*, *b*, and *c* values out of this. To start, it reads the first digit

__1__ 311240515664530744535140535140537114458924314452283453711453914253514053014043340

In this case, it is *1*. This tells the program to read the next *1* digit(s), and set it as the *a* value

1 __3__ 11240515664530744535140535140537114458924314452283453711453914253514053014043340

The *a* value is *3*

<br />
<br />

The program then reads the next digit

13 __1__ 1240515664530744535140535140537114458924314452283453711453914253514053014043340

It is *1*, this means the program is reading the next *1* digit(s), and setting it as the *b* value

131 __1__ 240515664530744535140535140537114458924314452283453711453914253514053014043340

The *b* value is 1

<br />
<br />

Finally, the program reads the next number, which is *2*

1311 __2__ 40515664530744535140535140537114458924314452283453711453914253514053014043340

This tells the program to read the next __2__ digits, and set that is the *c* value

13112 __40__ 515664530744535140535140537114458924314452283453711453914253514053014043340

The *c* value is *40*

<br />
<br />
<br />
<br />

From here, the *a*, *b*, and *c* values have been figured out. The program can now start decrypting the actual message. To decrypt the first letter, it reads the next digit

1311240 __5__ 15664530744535140535140537114458924314452283453711453914253514053014043340

<br />

This tells the program to read the next *5* digits, which in this case is __15664__

13112405 __15664__ 530744535140535140537114458924314452283453711453914253514053014043340

<br />
<br />

Here is the equation that the decrypter has discovered 

*3x<sup>2</sup> + 1x + 40 = 15664*

To figure out the original number, we set the equation equal to zero.

*3x<sup>2</sup> + 1x - 15624 = 0*

Then, we apply the quadratic equation and take the result that is achieved when you __add__ the square root of *b<sup>2</sup> - 4ac* to *-b*

The result is 72, which is a capital H in ASCII decimal. The program converts the 72 to "H", and moves on to find the next character. The entire string of digits spells out, "Hello, World!"

<br />
<br />
<br />
<br />

# How the encrypter works
When you run the encrypter, it creates a randomly generated *a*, *b*, and *c* value. You can how random these values are if you like. They are set quite low so the encrypted message isn't huge.

The encrypter looks at each character in the string you provide it, finds it's ASCII decimal value, and then plugs it into the equation *ax<sup>2</sup> + bx + c*. The program then spits out a new number. These new numbers are strung together to create a long, and very large number.

You can type the same message into the encrypter each time you run it, and it should spit out a completely random and unique string of digits. This is because the *a*, *b*, and *c* value are selected randomly each time you run the encrypter.
