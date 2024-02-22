// Help me to integrate the following to the above.
// year="1986"
// month="6"
// day="10"
// hr="14"
// minute="30"
// gender="F"
// # select = Select(driver.find_element(By.NAME, "hityear"))
// # select.select_by_value(year)

// # select = Select(driver.find_element(By.NAME, "hitmonth"))
// # select.select_by_value(month)

// # select = Select(driver.find_element(By.NAME, "hitday"))
// # select.select_by_value(day)

// # select = Select(driver.find_element(By.NAME, "hittime"))
// if gender == "M":
//     driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='1']").click()
// elif gender =="F":
//     driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='0']").click()
//     # "input[type='radio'][value='0']").click()

// submit=driver.find_element(By.CSS_SELECTOR, "input[type='submit'][id='submitb']")
// #scroll to submit button
// driver.execute_script("arguments[0].scrollIntoView();", submit)

// submit.click()

const puppeteer = require("puppeteer");

(async () => {
  // Define variables for year and month
  const selectedYear = "1986";
  const selectedMonth = "6";
  const selectedDay = "10";
  const selectedHour = "14";
  const selectedMinute = "30";
  const selectedGender = "F";

  // Launch a headless browser
  const browser = await puppeteer.launch({ headless: false });
  // launch({ headless: false }) to see the browser in action

  // Open a new page
  const page = await browser.newPage();

  // Navigate to the website
  await page.goto("https://fatew.com/star/");

  // Wait for the select elements to be available
  await page.waitForSelector('select.mybirth[name="hityear"]');
  await page.waitForSelector('select.mybirth[name="hitmonth"]');
  await page.waitForSelector('select.mybirth[name="hitday"]');
  await page.waitForSelector('select.mybirth[name="hittime"]');

  if (selectedGender === "M") {
    await page.click('input[type="radio"][value="1"]');
  } else if (selectedGender === "F") {
    await page.click('input[type="radio"][value="0"]');
  }

  // Select the year element
  const yearSelect = await page.$('select.mybirth[name="hityear"]');
  // Select the month element
  const monthSelect = await page.$('select.mybirth[name="hitmonth"]');
  const daySelect = await page.$('select.mybirth[name="hitday"]');
  const hourSelect = await page.$('select.mybirth[name="hittime"]');

  // Select the year variable
  await yearSelect.select(selectedYear);
  // Select the month variable
  await monthSelect.select(selectedMonth);
  await daySelect.select(selectedDay);
  await hourSelect.select(selectedHour);

  // Wait for a brief moment to ensure the options are selected
  await new Promise((resolve) => setTimeout(resolve, 1000));

  // Get the value of the selected year and month
  const actualYear = await page.$eval(
    'select.mybirth[name="hityear"]',
    (element) => element.value
  );
  const actualMonth = await page.$eval(
    'select.mybirth[name="hitmonth"]',
    (element) => element.value
  );
  const actualDay = await page.$eval(
    'select.mybirth[name="hitday"]',
    (element) => element.value
  );
  const actualHour = await page.$eval(
    'select.mybirth[name="hittime"]',
    (element) => element.value
  );

  // Check if the selected year and month match the variables
  if (
    actualYear === selectedYear &&
    actualMonth === selectedMonth &&
    actualDay === selectedDay &&
    actualHour === selectedHour
  ) {
    console.log("Options selection successful.");
    // Click the submit button
    await page.click('input[type="submit"][id="submitb"]');
    //
    // Wait for a brief moment to ensure the options are selected
    await new Promise((resolve) => setTimeout(resolve, 1000));
    //get the text of desired elements

    const comments = await page.$$eval(".comment", (elements) =>
      elements
        .map((element) => element.textContent.trim().replace(/\n{2,}/g, "\n")) // Remove consecutive empty lines
        .filter((comment) => comment !== "")
    );

    console.log(comments);

    // Get the HREF
    async function extractLinks(page, selector) {
        const links = await page.$$eval(selector, elements =>
            elements.map(element => ({
                text: element.textContent.trim(),
                href: element.getAttribute('href')
            }))
        );
        const linkMap = {};
        links.forEach(link => {
            linkMap[link.text] = link.href;
        });
        return linkMap;
    }
    
    // Usage
    const links = await extractLinks(page, 'a');
    console.log(links);
    

  } else {
    console.error("Options selection failed.");
  }

  // Close the browser
  //   await browser.close();
})();
