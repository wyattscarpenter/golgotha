🔣💀
GOLGOTHA: Define new operators in any language. Do it, coward! Do it now!

Golgotha is a preprocessor for source texts that allows you to define new infix (or prefix or postfix) operators using rules like this:

🔣1$2🔜2-1

This example would result in all statements like a$b being transformed to b-a.

This is mostly useful for rules like:

🔣1⋅2🔜1.dot(2)

in languages that don't support the correct operators you want.

Most of the time, you'll want the golgotha rule to be as small as possible, and just perform the syntactic sugar transform to a function call defined elsewhere.

All Golgotha rules must start on a new line, and begin with 🔣. They are terminated by a newline as well. Other whitespace is not stripped, although the golgotha rule will be interpreted as though each argument may be surrounded by arbitrary amounts of whitespace. Arguments are represented in the rules by single numeric characters.

Golgotha rules are applied in the source text even before they are specified, because the Golgotha processing of the source text is double-pass. However, Golgotha rules are still applied in the ORDER they are specified, so you should put more specific forms first so they can be applied before more general forms. If you have both a $ and a $= operator, specify the $= first.

Golgotha has no concept of precedence. This is because it is permissible to apply Golgotha rules to a language text that already has infix operators, and we don't want you to have to respecify those to get correct precedence behavior overall. Therefore all transformations must be fully parenthesized, unless you want the default behavior, which is just always operating on the closest "word" strings. Golgotha has an inherent idea of what characters parenthesize in the sense above. These "parenthors" are (), [], and {}.

In classic applications, word characters would be defined as the alphanumerounderscorics. However, since we live in the future, they're probably actually defined as anything Unicode thinks of as a letter, a digit, or a connector (which includes underscores). For convenience, Golgotha also includes "." as a word character, due to the popularity of that character as the "dot" member access operator (not to be confused with any "dot" scalar product operator), so that eg person1.name ∘ person2.name operates on both of those entities as intended, and not on "name" and "person2" alone.

Golgotha has been engineered to be easy to implement more than anything else. The current implementation is in Python 3. But a faster implementation would probably be easy to make in another language, and probably should be made before Golgotha is integrated into your build pipeline.

Golgotha is implicitly UTF-8. Also implicitly, we just assume you don't want to deal with any Golgotha rule symbols (🔣🔜) in the non-Golgotha parts of your program. There is currently no explicit mechanism to deal with that. However, Golgotha symbols on lines not beginning with 🔣 will be ignored, so it's a constrained edge case.

Golgotha+ is an UNIMPLEMENTED extension to Golgotha which would allow one to set the word character set with 🔠 lines (default 🔠ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_ except actually the default would be unicode \w behavior probably, which would be much harder to replicate with a 🔠 line); the argument (in 🔣 rule lines) character set with 🔢 lines (default 0123456789); and the set of parenthors with 🅿🔚 lines (default 🅿(🔚), 🅿[🔚], and 🅿{🔚}). I was going to implement Golgotha+ but then I realized that no one was going to use this software anyway so the use case was literally 0. An instance of Golgotha with Golgotha+ rules applied to overwrite defaults may be called a Golgothoid.

This Golgotha (name picked at random) is not to be confused with the R Natural Language Processing package Golgotha https://github.com/bnosac/golgotha nor the video game / game engine Golgotha https://github.com/videogamepreservation/golgotha / https://github.com/pgrawehr/golgotha
