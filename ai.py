import asyncio
from dotenv import load_dotenv

load_dotenv()
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

task = """
### AI Agent Task: End-to-End SauceDemo Purchase & Logout Workflow

#### Objective:
Automate a complete user journey on the SauceDemo website, including login, product selection, cart verification, removing items from the cart, return to home, and logout.

---

### Step 1: Login to SauceDemo

1. Open https://www.saucedemo.com.
   - Wait until the page fully loads before proceeding.
   - If loading takes too long, retry up to 3 times before failing.
2. Locate the username and password fields.
   - If either field is not found, log an error and stop execution.
3. Enter the credentials:
   - Username: standard_user
   - Password: secret_sauce
4. Click the Login button.
   - Wait for the products page to load.
   - If login fails, log an error and stop execution.

---

### Step 2: Add Product to Cart

1. On the products page, locate the first product.
   - If no products are found, log an error and stop execution.
2. Click the Add to cart button for the first product.
   - Wait for the cart badge to update, indicating an item was added.
   - If the cart badge does not update, log an error and stop execution.

---

### Step 3: Verify Cart Contents

1. Click the Cart icon (usually in the top-right corner).
   - Wait for the cart page to load.
2. Verify that the selected product appears in the cart.
   - If the product is missing, log an error and stop execution.

---

### Step 4: Remove Product from Cart

1. On the cart page, locate the Remove button for the product in the cart.
   - If the Remove button is not found, log an error and stop execution.
2. Click the Remove button to remove the product from the cart.
   - Wait for the product to disappear from the cart.
   - Verify the cart is empty after removal.
   - If the product is not removed, log an error and stop execution.

---

### Step 5: Return to Home (Products) Page

1. Locate and click the "Continue Shopping" or "Back to Products" button.
   - Wait for the products page to reload.
   - If the button is not found, log an error and stop execution.

---

### Step 6: Logout

1. Open the menu (usually a hamburger icon in the top-left).
   - Wait for the menu to expand.
2. Click the Logout option.
   - Wait for the login page to reappear.
   - If logout fails, log an error and stop execution.

---

### Step 7: Close the Browser

1. Wait for 5 seconds after logout to ensure the process is complete.
2. Close the browser window.

---

### Key Requirements & Error Handling

- Ensure each page loads fully before interacting with elements.
- Verify the presence of required UI elements before performing actions.
- Do not skip required user interactions (clicking, typing, confirming).
- Log errors and stop execution if any critical step fails.
- Handle credentials securely and avoid exposing sensitive information.
"""


async def main():
    # agent = Agent(
    #     task=(
    #         "1. Go to https://www.saucedemo.com. "
    #         "2. Enter username 'standard_user' and password 'secret_sauce' and log in. "
    #         "3. On the products page, click 'Add to cart' for the first product. "
    #         "4. Wait for 5 seconds. "
    #         "5. Close the browser."
    #     ),
    #     llm=ChatGoogleGenerativeAI(model='gemini-2.5-pro', temperature=1.0),
    # )

    agent = Agent(
        task=task,
        llm=ChatGoogleGenerativeAI(model='gemini-2.5-pro', temperature=1.0),
    )

    await agent.run()


asyncio.run(main())
