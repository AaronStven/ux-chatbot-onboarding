# Usability Study: Findings & Recommendations

## 1. Executive Summary
We tested three chatbot onboarding flows with 12 participants. **Prototype B (Carousel/Buttons)** significantly outperformed the others in both task speed and user satisfaction, while Prototype A (Text-heavy) caused the highest cognitive load.

## 2. Quantitative Results

| Prototype | Avg. Time on Task | Avg. Errors | Avg. SUS Score | Avg. NASA-TLX (Workload) |
| :--- | :--- | :--- | :--- | :--- |
| **A (Text-heavy)** | 49.0s | 2.0 | 65.0 | 62.9 |
| **B (Buttons)** | 25.7s | 0.5 | **84.1 (A)** | **30.8** |
| **C (Conversational)** | 38.3s | 0.8 | 74.9 | 43.3 |

*(Note: SUS > 80 is considered an "A" grade in usability).*

## 3. Qualitative Themes
- **Theme 1: "I don't know what to type."** Users in Prototype C struggled because they didn't know the chatbot's capabilities.
- **Theme 2: Option Paralysis.** Prototype A overwhelmed users with a massive wall of text.
- **Theme 3: Instant Gratification.** Users strongly preferred Prototype B because buttons allowed them to complete tasks in one or two clicks.

## 4. Design Recommendations
1. **Combine B and C:** Use a hybrid approach—start with buttons/carousels (Prototype B) to guide the user, but allow free-text typing once the conversation starts.
2. **Clear Input Affordance:** Add placeholder text like "Type your question here..." in the input field.
3. **Progressive Disclosure:** Do not show all campus services at once. Group them by category (e.g., "Academics", "Campus Life").