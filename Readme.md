# Anonymous lettering for Light IT portal

This is more user-friendly (but more ugly) solution, because user should not remember id of letter, besides codeword.
But, it solution have a big problem - if two users create letters with similar codewords - during retrieving their responds we doesn't know which respond(letter) for whom.

| Method | Endpoint                     | Availability | Method parameters  | Additional                                                                             |
| ------ | ---------------------------- | ------------ | ------------------ | -------------------------------------------------------------------------------------- |
| GET    | `/letters/`                  | For boss     | -                  | The "response__isnull" filter works for getting unanswered letters                     |
| POST   | `/letters/`                  | For all      | "text", "codeword" | Codeword and returned id of letter must be remembered by user for retrieving response. |
| PATCH  | `/letters/<id>/`             | For boss     | "response"         | -                                                                                      |
| POST   | `/letters/check/`            | For all      | "codeword"         | -                                                                                      |
