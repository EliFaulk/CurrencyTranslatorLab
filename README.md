# Currency Translator
This Python class uses a given dictionary of currency exchange rates to convert between currency values.


| Class Name | CurrencyConverter |
| - | - |
| Variables | currencies: dictionary |
| Methods | \_\_init__(currencies) <br>convert(amount, from_currency, to_currency) <br>add_rate(currency, rate) | 

## Example
```
example_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.78,
    "JPY": 150.50,
    "INR": 83.30
}

converter = CurrencyConverter(example_rates)

# Convert (100) USD into (92) euros
cash = 100
cash = converter.convert(cash, "USD", "EUR")

# Convert (92) euroes into (15,050) Japanese yen
cash = converter.convert(cash, "EUR", "JPY")

# Add Canadian dollars as a rate, then convert (15,050) Japanese yen into (136) Canadian dollars
converter.add_rate("CAD", 1.36)
cash = converter.convert(cash, "JPY", "CAD")

# Converter won't work if currency rates don't exist or if amount given is negative
cash = converter.convert(cash, "CAD", "IND")
```

## Setting Up Automated Testing (with GitHub Actions)
1. GitHub Actions looks for the *.github* folder in your project. Start by creating a new directory called *.github*
2. Move into the *.github* directory, then create another folder called *workflows*.

![Alt text](Screenshot%20From%202026-08-27%2014-16-48.png)

3. Move into the *workflows* directory, then create a new file called *run-tests.yml*
4. In *run-tests.yml*, copy the following code. This is the workflow itself, written in YAML. If you want to run the tests on another branch, change *"main"* to the desired branch.

```
# .github/workflows/run-tests.yml

name: Python Unit Tests

# This tells GitHub to run the workflow when code is pushed to the 'main' branch,
# or when a Pull Request is opened against the 'main' branch.
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    # This specifies the operating system for the virtual machine running your code
    runs-on: ubuntu-latest

    steps:
    # Step 1: Check out your repository's code onto the runner
    - name: Check out repository code
      uses: actions/checkout@v4

    # Step 2: Set up the Python environment
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.11" # You can change this to match your local version

    # Step 3: Install pytest (and any other requirements)
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
        # If you add a requirements.txt later, you would uncomment the line below:
        # pip install -r requirements.txt

    # Step 4: Execute the tests
    - name: Run tests with pytest
      run: |
        pytest -v
```

5. Add, commit, and push your changes to GitHub. GitHub should automatically detect the workflow and run your tests. 

![](Screenshot%20From%202026-08-27%2014-27-18.png)

6. To verify that the tests were run and to see the results, go to your repository on GitHub and navigate to the *Actions* tab. The workflow results should appear under the name of the message in your commit. 

![](Screenshot%20From%202026-08-27%2014-29-34.png)

7. Click on the workflow and select the green checkmark labeled *test* to view the results of the tests. These will run again every time that a commit is made. Tests can be added to the pytest file to run more on every commit.

![](Screenshot%20From%202026-08-27%2014-30-40.png)
