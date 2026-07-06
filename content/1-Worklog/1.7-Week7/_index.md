---
title: "Worklog Week 7"
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:
* Integrate the ReactJS frontend layout with Spring Boot Backend RESTful APIs.
* Deploy a complete user authentication and authorization workflow utilizing JWT bearer tokens.
* Conduct integration testing for core Pet Shop operational modules (Shopping Cart, Pet Spa Booking, Order Creation).

### Tasks carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | - Connect React frontend rendering components with Spring Boot APIs via the managed layer `services/api.js`.<br>- Configure Axios base URL properties to point precisely to the backend server endpoint location. | 01/06/2026 | 01/06/2026 | Axios & Spring Boot API Docs |
| 2 | - Construct full user Login/Registration workflows on the `LoginPage` and `RegisterPage` interfaces.<br>- Integrate backend JWT token handlers (`JwtResponse`, `JwtTokenProvider`) from `AuthController` into frontend `authStore.js` to manage active sessions and encapsulate controlled routes (`ProtectedRoute`, `AdminRoute`). | 02/06/2026 | 02/06/2026 | Spring Security & React Context |
| 3 | - Bind item catalog components (`ProductsPage`, `ProductCard`) with dynamic data arrays served by `ProductController`.<br>- Deploy frontend state logic for the `CartPage` via `cartStore.js`, syncing cart status synchronously with the backend `CartController`. | 03/06/2026 | 03/06/2026 | React State Management |
| 4 | - Develop processing workflows for checkout operations (`CheckoutPage`) and pet care appointment scheduling (`BookingPage`).<br>- Map communication pipelines from the user interface down to functional backend controllers including `OrderController` and `BookingController`. | 04/06/2026 | 04/06/2026 | Spring Boot Controller Mapping |
| 5 | - Perform comprehensive End-to-End testing across the global user lifecycle: Registration -> Login -> Cart operations -> Grooming booking (`SpaServiceController`) -> Invoice finalization.<br>- Optimize the backend `CorsConfig` file on Spring Boot to thoroughly handle cross-origin resource sharing (CORS) blocks between the two environments. | 05/06/2026 | 05/06/2026 | Integration Testing Guide |

### Week 7 Achievements:

* **Successful Multi-tier Architecture Integration:**
  * Established seamless communication between the ReactJS client application and Spring Boot RESTful APIs through a centralized `services/api.js` communication layer.
  * Configured unified system error handling to feed precise visual feedback back to end-users whenever an API request failure occurs.

* **Completed Authentication & Authorization Hardening:**
  * New users can now register accounts smoothly, with password hashing utilities automatically executing before persistent storage in the database.
  * Login/Logout mechanisms function stably; JWT tokens are securely parsed and attached to every outbound request header via the backend `JwtAuthenticationFilter` execution chain.
  * Strictly enforced admin-level route guarding: management dashboard interfaces (`AdminBookingsPage`, `AdminProductsPage`, `DashboardPage`) are fully isolated via frontend `AdminRoute` definitions, completely mitigating unauthorized standard user access.

* **Actualized Core Business Logic for the Pet Shop System:**
  * **Dynamic Catalog Rendering:** Merchandise profiles and pet care service catalogs load dynamically via the `ProductController` and `SpaServiceController` pipelines.
  * **Cart Ecosystem (`cartStore.js`):** Enabled item additions, absolute removals, quantity adjustments, and automated order subtotal calculations.
  * **Orders & Bookings Processing:** Finished data-binding routines to log persistent transactional schemas into order registries (`OrderController`) and reservation logs (`BookingController`).

* **Verified End-to-End User Journey Operations:**
  * Validated the standard user operation lifecycle: new account registration -> account login -> exploring available Spa services -> appending dry food supplies to cart -> completing appointment booking and generating invoicing logs.

* **Enhanced UX Feedback Loops & Conflict Refinement:**
  * Mitigated native cross-origin resource conflicts by optimizing cross-origin request mappings inside the backend Spring Boot `CorsConfig` repository.
  * Implemented systemic loading state visual elements onto client layouts to refine user interface responsiveness during remote server calls.