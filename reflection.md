# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, the game’s interface appeared functional. It featuring difficulty settings (like Normal for 1-100), an input field for guesses, a "New Game" button and a "Hint" button. The first bug I noticed were the incorrect hints. I expected that if my guess was higher than the secret number, the game should tell me to guess "lower" or the opposite in an alternate case. The hints were actually wrong most of the time. During a Normal difficulty game, the secret number was 11. However, the game continuously told me to go "higher" until I reached 100. The second bug I noticed was that the "New Game" Button failed to reset the state of the game. I expected that clicking the "New Game" button after winning or running out of guesses would reset the guess counter and allow me to play a new round. What actually happened was the button did not properly reset the game. Instead of starting over, it leaves the game locked in its end state. It would display prompts like "You already won. Start a new game to play again" or "Game over. Start a new game to try again" without actually initializing a new session. The third bug I noticed was that the secret numbers that were being generated were out of bounds. My expectation for this was The generated secret number should always fall strictly within the minimum and maximum limits of the selected difficulty. 


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

In this project, I created multipel chats with Copilot in order to debug the glithes within the guessing game. On example of an AI suggestion that was correct was refactoring the core game logic (range selection, guess parsing, and scoring) into a separate logic_utils.py file to clean up the main Streamlit script. It specifically provided the logic for parse_guess to handle string-to-integer conversion. I ran the game and entered various inputs, including empty strings and text. The game correctly caught the "Not a number" errors and successfully converted the decimal input "10.5" into the integer 10, preventing a crash. I also verified that the sidebar difficulty correctly changed the low and high values used for the secret number. An example of an AI suggestion that was incorrect or misleading was suggesting a partial reset when tring to generate the "New Game" button logic. noticed that after winning a game and clicking "New Game," the app would freeze. I traced this back to st.session_state.status remaining as "won," which triggered the st.stop() guard clause. This proved the AI forgot to reset the game status to "playing." I observed the attempt counter which started. at 0 instead of 1. This, in turn, messed up the scoring math. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed only when it was proven the game's behavior matched the intended logic across multiple rounds. For example, there was an instance a fix wasn't "done" just because the first game worked. I had to trigger a "Win" or "Loss" state and then click "New Game" to ensure the st.session_state.status reset correctly and didn't trigger an accidental st.stop(). I ran a manual test, where I set the difficulty to "Easy" and played one round. After clicking "New Game," I checked if the new secret was still within that range. Initially, the AI's code caused the "Easy" setting to be ignored after the first game. By correcting this to use the low and high variables from get_range_for_difficulty, I ensured the difficulty setting persisted. The AI helped me understand the ImportError I encountered with the pytest. It explained that pytest couldn't find my logic_utils module because of the directory structure. After realizing I had to refactor logic into the different functions of the logic_utils module, this allowed my test to actually run and pass.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
