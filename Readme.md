# Anonymous lettering for Light IT portal

| Method | Endpoint                     | Availability | Method parameters  | Additional                                                                             |
| ------ | ---------------------------- | ------------ | ------------------ | -------------------------------------------------------------------------------------- |
| GET    | `/letters/`                  | For boss     | -                  | The "response__isnull" filter works for getting unanswered letters                     |
| POST   | `/letters/`                  | For all      | "text", "codeword" | Codeword and returned id of letter must be remembered by user for retrieving response. |
| PATCH  | `/letters/<id>/`             | For boss     | "response"         | -                                                                                      |
| POST   | `/letters/<id>/check/`       | For all      | "codeword"         | Id also passed by user.                                                                |
