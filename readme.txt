🔣💀
GOLGOTHA: Define new operators in any language. Do it, coward! Do it now!

Golgotha is a preprocessor for source texts that allows you to define new infix (or prefix or postfix) operators using rules like this:

🔣1$2🔜2-1

This example would result in all statements like a$b being transformed to b-a. Whitespace is ignored.

This is mostly useful for rules like:

🔣1⋅2🔜1.dot(2)

in languages that don't support the correct operators you want.

Most of the time, you'll want the golgotha rule to be as small as possible, and just perform the syntactic sugar transform to a function call defined elsewhere.

All Golgotha rules must start on a new line, and begin with 🔣. They are terminated by a newline as well. Arguments are represented by single alphanumeric characters.

Golgotha rules are applied in the source text only after they have been specified.

Golgotha rules are applied in the order they are specified, so you should put more specific forms first so they can be applied before more general forms. If you have both a $ and a $= operator, specify the $= first.

Golgotha has no concept of precedence, and all transformations must be fully parenthesized! Unless you want the default behavior, which is just always operating on the closest alphanumeric strings. This is because it is permissible to apply Golgotha rules to a language text that already has infix operators, and we don't want you to have to respecify those.

Golgotha also has no inherent idea of what characters parenthesize in the sense above, so you must specify parenthors like so:

🅿(🔚)
🅿[🔚]
🅿{🔚}

Those are some good ones to start you off. 

Golgotha has been engineered to be easy to implement more than anything else.

The current implementation is in Python 3. But a faster implementation would probably be easy to make, and should be made before Golgotha is integrated into your build pipeline.

Golgotha is implicitly UTF-8. Also implicitly, we just assume you don't want to deal with any Golgotha rule symbols (🔣🔜🅿🔚) in the non-Golgotha parts of your program. There is currently no explicit mechanism to deal with that. However, Golgotha symbols on lines not beginning with 🔣 or 🅿 will be ignored, so it's a constrained edge case.

This Golgotha (name picked at random) is not to be confused with the R Natural Language Processing package Golgotha https://github.com/bnosac/golgotha nor the video game / game engine Golgotha https://github.com/videogamepreservation/golgotha / https://github.com/pgrawehr/golgotha
