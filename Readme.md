# Anonymous lettering for Light IT portal

The flow of lettering:
1. User input text and codeword for letter. He must remember codeword and returned id of letter
2. User periodically checks his letter for response by passing id and codeword if form
3. Boss get list of unanswered letters
4. Boss responds to letters
5. Profit

This flow is not very user-friendly, because user must to remember id of letter, besides codeword.
This repository has branch "without-id" that implements flow, without having to remember id of letter.
But this implementation has a problem - if two users create letters with similar codewords - during retrieving their responses we doesn't know which response(letter) for whom.
If we can find way how to bypass this - "without-id" realization will be better.


| Method | Endpoint                     | Availability | Method parameters  | Additional                                                                             |
| ------ | ---------------------------- | ------------ | ------------------ | -------------------------------------------------------------------------------------- |
| GET    | `/letters/`                  | For boss     | -                  | The "response__isnull" filter works for getting unanswered letters                     |
| POST   | `/letters/`                  | For all      | "text", "codeword" | Codeword and returned id of letter must be remembered by user for retrieving response. |
| PATCH  | `/letters/<id>/`             | For boss     | "response"         | -                                                                                      |
| POST   | `/letters/<id>/check/`       | For all      | "codeword"         | Id also passed by user.                                                                |
