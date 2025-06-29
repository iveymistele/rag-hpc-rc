## The Main File, app.R

Go to **projects** -> **project0-first-app** and open **app.R**.

- This file contains all the components of the app: the user interface and reactive logic.

- The UI and reactive logic can be written in separate .R files that are sourced in `app.R` or all put in the same file. 

- In this case the UI is in `user_interface.R` and the reactive logic is in `reactive_logic.R`.

<br>

## shinyApp()

`app.R` is just a regular R script

- Adding the call to `shinyApp()` at the end of the script changes the "Run" button to "Run App"

## Starting in the Muggle World

Let's start with `muggle.R` (our run-of-the-mill R code)

- We load the libraries we need

- We create a function `muggle_plot` that takes variable names from the `diamonds` dataset as inputs and generates a scatterplot

- Test it out if you want by uncommenting and running the last line of the script

## User Interface

Open `user_interface.R`

- The function `tagList` takes HTML functions as inputs and creates a list of HTML components

- Try running the first line, `h2("A very basic Shiny app")` in the console (make sure you have `shiny` loaded)

- Functions like `h2`, `p`, and `actionButton` are wrappers for HTML code (essentially strings)

- The first argument in `actionButton`, `plotOutput`, and `textOutput` are IDs. We will use these IDs in the next part


## Reactive Logic

Open `reactive_logic.R`

- We will connect the UI to the Muggle code with **reactive logic**

- We are assigning a function to `reactive_logic` with three arguments: `input`, `output`, and `session`. The arguments are always the same, but `reactive_logic` is usually called `server`.

- Functions `renderPlot` and `renderText` are assigned to `output$IDname`. They correspond to the UI functions `plotOutput` and `textOutput`


## Invoking the App

`shinyApp(user_interface, reactive_logic)`

To run our app, we use the command `shinyApp`. The first argument is the UI, and the second argument is our reactive logic.


## Deploying the App

1. Put all the files your app needs in a single directory (the name of the directory will be the name of the app)

2. Make sure there is a file called `app.R` with the call to `shinyApp()`

3. Run `rsconnect::deployApp("/path/to/app/directory")`. You may need to connect your shinyapps.io account to deploy an app for the first time.


## Your Turn: Modify the App

Try the following on your own!

1. Hide the button message until the button has been clicked 3 times.

2. Add `selectInput` dropdown menus for the X and Y variables.

3. (Superstar) Connect the `selectInput` menus to the plot (we haven't covered this yet)
