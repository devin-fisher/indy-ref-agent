# Design Concepts
## Goals
### Can Host an Identity

 - [ ] List item

The reference agent should be fully functional. Meaning it could be used to host my identity in production (in my basement). But it may be slow or not able to scale.
- 1 Identity, 1 wallet

But the agent cannot be crippled. It must function using Sovrin best practices:
- Keys at edge
- Encryption at Rest
- 
### Readily Hackable
The code structure must allow additional agent functionality. Adding this functionality must be easy and quick. 
The coding language should support this goal. This agent is using python.
### Provide Implementation of Sovrin Protocol
The ref agent should inform the community about the quality of the designed and/or proposed protocol. As such, multiple versions of the agent may be required.
### Test Suite
The ref agent should provide a test suite that tests other agent's compliance to the Sovrin Protocol.

## Trade-Offs
### Simplicity and Exendabilty over Scalability and Performance
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMwMTk1NjUxOF19
-->