---
id: DOC-B1
title: Handling of the invented Kestrel score
corpus: graph-provenance-explorer synthetic corpus v1
---

> Authored synthetic material. Fictional identifiers and invented workflow terms.
> Not clinical guidance. Not derived from any patient, dataset, guideline, or person.

[p1] The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[p2] The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[p3] A line whose Kestrel score is K0 must be withheld from the released summary. In its place the renderer emits the standard abstention sentence and nothing else, so that a reader can see that a line was considered and set aside rather than silently dropped. This handling follows the fictional Harrowgate working note on unsupported lines and is not to be relaxed at desk level.
