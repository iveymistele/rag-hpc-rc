## Shiny Bridges Two Worlds of R Programming

In Harry Potter, the Knight Bus connected the non-magical, or "Muggle", world to the magical Wizarding World. Similarly, Shiny connects regular R code to the magical world of "reactives" (we will talk more about these later).

| 1. **Muggle World**        | 2. **Wizarding World**    |
|         ---                |           ---             |
| - Regular R code           | - Reactives               |
| - Functions, packages, etc | - Functions w/o arguments |
|                            | - Values that can't be changed with **`<-`** |
|                            | - Packaged in a `server` function |

The Wizarding world can reach out to the Muggle world, but not the other way around.
