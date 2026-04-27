### **TC-01: Verification of event search by keyword (Positive)**

**Preconditions:**
* The user has opened the [GreenCity Events](https://www.greencity.cx.ua/#/greenCity/events) page.
* Existing events are present in the system (e.g., an event titled "Some Event").

**Test Steps:**

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Enter the event title into the "Search" field | "Some Event" | The list updates to display only events containing the specified phrase. |
| 2 | Clear the text from the search field | Empty string | The search filter is removed, and the full list of events is displayed again. |

---

### **TC-02: Verification of event filtering by type (Positive)**

**Preconditions:**
* The user is on the "Events" page.

**Test Steps:**

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Click on the "Статус" filter button | - | A dropdown menu appears with "Відкрита" and "Закрита" options. |
| 2 | Select the "Відкрита" option | Option "Відкрита" | Only active events available for joining are displayed on the page. |
| 3 | Change the filter selection to "Закрита" | Option "Закрита" | The list updates to show only events that have already ended or are closed. |

---

### **TC-03: Search for non-existent event (Negative)**

**Preconditions:**
* The user is on the "Events" page.

**Test Steps:**

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Enter a random string of symbols into the search bar | "XYZ123!@#" | The system processes the request. |
| 2 | Observe the search results area | - | The list is empty, and a message like "No events found" or an empty state illustration is displayed. |

---
### **TC-04: Redirection to login when trying to "Join" as a guest (Negative)**

**Preconditions:**
* The user is not logged in.
* The user is on an event detail page.

**Test Steps:**

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Locate the "Приєднатися до події" button on the event page | - | The button is visible or active. |
| 2 | Click on the "Приєднатися до події" button | - | The system does not register the user but instead opens the Login/Sign-in modal or redirects to the Login page. |