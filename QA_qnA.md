# QA Scenario Based Questions
1. Sprint velocity is dropping due to flaky automation tests. How would you handle this?
If the sprint velocity is dropping because of flaky tests, the first step I would take is to identify the root cause of the flakiness. 
Flaky tests usually occur due to unstable locators, synchronization issues or environment instability.
I would start by analyzing the failing tests in CI to understand patterns. If certain tests are failing intermittently, I would prioritize stabilizing them by improving waits, using more reliable locators, and ensuring proper test isolation.
At the same time, I would ask the team to temporarily mark highly unstable tests so they do not block the pipeline, while we fix them in parallel. Completely removing them from execution is not ideal, but we should ensure they do not impact the team's productivity.
Another step is improving our automation practices such as:
- Using better synchronization methods instead of static waits
- Running tests in stable environments
- Adding proper logging and screenshots for debugging
I would also schedule a short team discussion to understand if there are gaps in our framework or test design that are causing these issues.
The goal is to gradually stabilize the automation suite so that it becomes reliable again and supports the team instead of slowing it down.

2. During a production release, two critical bugs are reported by the client that were missed in QA. How would you address the gap?
If critical bugs are found in production, the first priority is to understand the impact and support the development team in verifying the fixes quickly.
After the immediate issue is handled, I would conduct a root cause analysis with the team. The goal is to understand why the defects were missed. Possible reasons could be gaps in test coverage, unclear requirements, edge cases not considered, or issues with the test environment.
Based on the findings, I would take several actions to improve the process. For example:
- Update or add new test cases to cover the missed scenarios
- Add these cases to our regression suite
- Improve requirement clarification during sprint planning
- Strengthen exploratory testing for high-risk features
- Improve communication between QA, developers, and product teams
I also believe production defects should be treated as learning opportunities rather than blame situations. The focus should always be on improving the testing process so that similar issues are less likely to occur in the future.
By continuously improving our test coverage, automation, and communication within the team, we can reduce the chances of critical bugs reaching production.