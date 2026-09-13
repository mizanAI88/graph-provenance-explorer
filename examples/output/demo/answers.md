# Demo answers (authored synthetic corpus v1)

Rendered by the deterministic TemplateRenderer. Every citation resolves to
examples/corpus/v1. Scores are BM25 or BM25 plus edge-weight bonuses on this
fixture and are not benchmark results.

## Q01: What range of values can the Marlow Index take?

Answerable: True. Gold: DOC-A1#p1

### mode=lexical

```
Question: What range of values can the Marlow Index take?
Mode: lexical

[DOC-A1#p1] (score 3.887; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-A1#p3] (score 3.769; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-F1#p2] (score 3.424; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-F1#p3] (score 3.218; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

[DOC-L1#p3] (score 3.177; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

Sources: [DOC-A1#p1], [DOC-A1#p3], [DOC-F1#p2], [DOC-F1#p3], [DOC-L1#p3]
```

### mode=graph

```
Question: What range of values can the Marlow Index take?
Mode: graph

[DOC-L1#p3] (score 3.977; DOC-L1#p3 -[refines]-> DOC-A1#p1)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-A1#p1] (score 3.887; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-A1#p3] (score 3.769; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-F1#p2] (score 3.424; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-F1#p1] (score 3.287; DOC-F1#p1 -[cites]-> DOC-A1#p1)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

Sources: [DOC-L1#p3], [DOC-A1#p1], [DOC-A1#p3], [DOC-F1#p2], [DOC-F1#p1]
```

### mode=vector

```
Question: What range of values can the Marlow Index take?
Mode: vector

[DOC-G1#p3] (score 0.319; direct lexical match)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

[DOC-A1#p1] (score 0.244; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-F1#p1] (score 0.241; direct lexical match)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

[DOC-A1#p3] (score 0.215; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-F1#p3] (score 0.151; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

Sources: [DOC-G1#p3], [DOC-A1#p1], [DOC-F1#p1], [DOC-A1#p3], [DOC-F1#p3]
```

## Q02: When is the Marlow Index recomputed?

Answerable: True. Gold: DOC-A1#p2, DOC-D1#p2

### mode=lexical

```
Question: When is the Marlow Index recomputed?
Mode: lexical

[DOC-A1#p2] (score 5.285; direct lexical match)
The Marlow Index is recomputed for every queued request at the start of each Osprey window. Recomputation by hand between windows is permitted only when the Wren ledger shows that the request has no entry for the previous window, and any hand recomputation must itself be written into the ledger with the initials of the reviewer who performed it. A recomputation that is not in the ledger is treated as if it had not happened.

[DOC-D1#p2] (score 4.504; direct lexical match)
Inside an Osprey window the desk performs three actions in a fixed order. First, the Marlow Index of every queued request is recomputed. Second, any Kestrel bands that are due under the Ferris loop schedule are refreshed. Third, the Wren ledger is reconciled so that every line touched during the window has an entry that names the window. The window closes with a closing entry, and no further action of these three kinds is taken until the next window opens.

[DOC-A1#p1] (score 3.887; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-A1#p3] (score 3.769; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-F1#p3] (score 3.218; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

Sources: [DOC-A1#p2], [DOC-D1#p2], [DOC-A1#p1], [DOC-A1#p3], [DOC-F1#p3]
```

### mode=graph

```
Question: When is the Marlow Index recomputed?
Mode: graph

[DOC-A1#p2] (score 5.785; DOC-D1#p2 -[cites]-> DOC-A1#p2)
The Marlow Index is recomputed for every queued request at the start of each Osprey window. Recomputation by hand between windows is permitted only when the Wren ledger shows that the request has no entry for the previous window, and any hand recomputation must itself be written into the ledger with the initials of the reviewer who performed it. A recomputation that is not in the ledger is treated as if it had not happened.

[DOC-D1#p2] (score 5.304; DOC-A1#p2 -[refines]-> DOC-D1#p2)
Inside an Osprey window the desk performs three actions in a fixed order. First, the Marlow Index of every queued request is recomputed. Second, any Kestrel bands that are due under the Ferris loop schedule are refreshed. Third, the Wren ledger is reconciled so that every line touched during the window has an entry that names the window. The window closes with a closing entry, and no further action of these three kinds is taken until the next window opens.

[DOC-L1#p3] (score 3.977; DOC-L1#p3 -[refines]-> DOC-A1#p1)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-A1#p1] (score 3.887; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-F1#p1] (score 3.287; DOC-F1#p1 -[cites]-> DOC-A1#p1)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

Sources: [DOC-A1#p2], [DOC-D1#p2], [DOC-L1#p3], [DOC-A1#p1], [DOC-F1#p1]
```

### mode=vector

```
Question: When is the Marlow Index recomputed?
Mode: vector

[DOC-A1#p1] (score 0.315; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-A1#p3] (score 0.278; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-G1#p3] (score 0.247; direct lexical match)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

[DOC-A1#p2] (score 0.217; direct lexical match)
The Marlow Index is recomputed for every queued request at the start of each Osprey window. Recomputation by hand between windows is permitted only when the Wren ledger shows that the request has no entry for the previous window, and any hand recomputation must itself be written into the ledger with the initials of the reviewer who performed it. A recomputation that is not in the ledger is treated as if it had not happened.

[DOC-F1#p3] (score 0.195; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

Sources: [DOC-A1#p1], [DOC-A1#p3], [DOC-G1#p3], [DOC-A1#p2], [DOC-F1#p3]
```

## Q03: Can the Marlow Index override an open Brindle flag?

Answerable: True. Gold: DOC-A1#p3

### mode=lexical

```
Question: Can the Marlow Index override an open Brindle flag?
Mode: lexical

[DOC-A1#p3] (score 10.415; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-A1#p1] (score 6.671; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-F1#p1] (score 6.101; direct lexical match)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

[DOC-E1#p3] (score 4.071; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-E1#p2] (score 3.980; direct lexical match)
Any reviewer may raise a Brindle flag, and raising one requires no approval. Only a Lantern review may clear a flag, and the person who raised the flag may not perform that review. A cleared flag is not deleted: it remains in the Wren ledger together with the closing note of the review that cleared it, so that a later reader can see both that a disagreement existed and how it was settled.

Sources: [DOC-A1#p3], [DOC-A1#p1], [DOC-F1#p1], [DOC-E1#p3], [DOC-E1#p2]
```

### mode=graph

```
Question: Can the Marlow Index override an open Brindle flag?
Mode: graph

[DOC-A1#p3] (score 10.415; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-A1#p1] (score 7.171; DOC-F1#p1 -[cites]-> DOC-A1#p1)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-F1#p1] (score 6.601; DOC-F1#p1 -[cites]-> DOC-A1#p1)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

[DOC-E1#p2] (score 4.980; DOC-A1#p3 -[supports]-> AST-03 -> DOC-E1#p2 -[supports]-> AST-03)
Any reviewer may raise a Brindle flag, and raising one requires no approval. Only a Lantern review may clear a flag, and the person who raised the flag may not perform that review. A cleared flag is not deleted: it remains in the Wren ledger together with the closing note of the review that cleared it, so that a later reader can see both that a disagreement existed and how it was settled.

[DOC-E1#p1] (score 4.229; DOC-A1#p3 -[cites]-> DOC-E1#p1)
The Brindle flag is an invented marker attached to a single summary line when two approved passages make statements about that line that cannot both be true. The flag names the line, the two passage identifiers, and the reviewer who noticed the conflict. A flag is never attached to a whole summary and never to a passage; it belongs to the line whose support is in dispute.

Sources: [DOC-A1#p3], [DOC-A1#p1], [DOC-F1#p1], [DOC-E1#p2], [DOC-E1#p1]
```

### mode=vector

```
Question: Can the Marlow Index override an open Brindle flag?
Mode: vector

[DOC-A1#p3] (score 0.541; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-A1#p1] (score 0.312; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-E1#p2] (score 0.268; direct lexical match)
Any reviewer may raise a Brindle flag, and raising one requires no approval. Only a Lantern review may clear a flag, and the person who raised the flag may not perform that review. A cleared flag is not deleted: it remains in the Wren ledger together with the closing note of the review that cleared it, so that a later reader can see both that a disagreement existed and how it was settled.

[DOC-G1#p3] (score 0.233; direct lexical match)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

[DOC-F1#p1] (score 0.220; direct lexical match)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

Sources: [DOC-A1#p3], [DOC-A1#p1], [DOC-E1#p2], [DOC-G1#p3], [DOC-F1#p1]
```

## Q04: How many bands does the Kestrel score have?

Answerable: True. Gold: DOC-B1#p1

### mode=lexical

```
Question: How many bands does the Kestrel score have?
Mode: lexical

[DOC-B1#p1] (score 5.742; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[DOC-E1#p3] (score 3.846; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-B1#p2] (score 3.531; direct lexical match)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-B1#p3] (score 3.531; direct lexical match)
A line whose Kestrel score is K0 must be withheld from the released summary. In its place the renderer emits the standard abstention sentence and nothing else, so that a reader can see that a line was considered and set aside rather than silently dropped. This handling follows the fictional Harrowgate working note on unsupported lines and is not to be relaxed at desk level.

[DOC-D1#p2] (score 3.227; direct lexical match)
Inside an Osprey window the desk performs three actions in a fixed order. First, the Marlow Index of every queued request is recomputed. Second, any Kestrel bands that are due under the Ferris loop schedule are refreshed. Third, the Wren ledger is reconciled so that every line touched during the window has an entry that names the window. The window closes with a closing entry, and no further action of these three kinds is taken until the next window opens.

Sources: [DOC-B1#p1], [DOC-E1#p3], [DOC-B1#p2], [DOC-B1#p3], [DOC-D1#p2]
```

### mode=graph

```
Question: How many bands does the Kestrel score have?
Mode: graph

[DOC-B1#p1] (score 5.742; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[DOC-E1#p3] (score 4.846; DOC-B1#p2 -[supports]-> AST-02 -> DOC-E1#p3 -[supports]-> AST-02)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-B1#p2] (score 4.531; DOC-E1#p3 -[supports]-> AST-02 -> DOC-B1#p2 -[supports]-> AST-02)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-K1#p1] (score 1.839; DOC-K1#p1 -[cites]-> DOC-B1#p1)
The Corvid audit is an invented periodic examination of released summaries. At each audit sitting the auditor draws a sample of released summaries, and for every line in the sample checks that each cited passage identifier resolves to a passage in the approved corpus, that the line has a Wren ledger entry, and that the recorded Kestrel band matches the number of cited passages that actually support the line.

Sources: [DOC-B1#p1], [DOC-E1#p3], [DOC-B1#p2], [DOC-K1#p1]
```

### mode=vector

```
Question: How many bands does the Kestrel score have?
Mode: vector

[DOC-B1#p1] (score 0.221; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[DOC-E1#p3] (score 0.209; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-B1#p3] (score 0.183; direct lexical match)
A line whose Kestrel score is K0 must be withheld from the released summary. In its place the renderer emits the standard abstention sentence and nothing else, so that a reader can see that a line was considered and set aside rather than silently dropped. This handling follows the fictional Harrowgate working note on unsupported lines and is not to be relaxed at desk level.

[DOC-B1#p2] (score 0.163; direct lexical match)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-D1#p2] (score 0.128; direct lexical match)
Inside an Osprey window the desk performs three actions in a fixed order. First, the Marlow Index of every queued request is recomputed. Second, any Kestrel bands that are due under the Ferris loop schedule are refreshed. Third, the Wren ledger is reconciled so that every line touched during the window has an entry that names the window. The window closes with a closing entry, and no further action of these three kinds is taken until the next window opens.

Sources: [DOC-B1#p1], [DOC-E1#p3], [DOC-B1#p3], [DOC-B1#p2], [DOC-D1#p2]
```

## Q05: How often is the Kestrel score recomputed?

Answerable: True. Gold: DOC-B1#p2, DOC-E1#p3

### mode=lexical

```
Question: How often is the Kestrel score recomputed?
Mode: lexical

[DOC-B1#p2] (score 5.933; direct lexical match)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-E1#p3] (score 3.846; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-B1#p1] (score 3.773; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[DOC-B1#p3] (score 3.531; direct lexical match)
A line whose Kestrel score is K0 must be withheld from the released summary. In its place the renderer emits the standard abstention sentence and nothing else, so that a reader can see that a line was considered and set aside rather than silently dropped. This handling follows the fictional Harrowgate working note on unsupported lines and is not to be relaxed at desk level.

[DOC-D1#p2] (score 3.227; direct lexical match)
Inside an Osprey window the desk performs three actions in a fixed order. First, the Marlow Index of every queued request is recomputed. Second, any Kestrel bands that are due under the Ferris loop schedule are refreshed. Third, the Wren ledger is reconciled so that every line touched during the window has an entry that names the window. The window closes with a closing entry, and no further action of these three kinds is taken until the next window opens.

Sources: [DOC-B1#p2], [DOC-E1#p3], [DOC-B1#p1], [DOC-B1#p3], [DOC-D1#p2]
```

### mode=graph

```
Question: How often is the Kestrel score recomputed?
Mode: graph

[DOC-B1#p2] (score 6.933; DOC-E1#p3 -[supports]-> AST-02 -> DOC-B1#p2 -[supports]-> AST-02)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-E1#p3] (score 4.846; DOC-B1#p2 -[supports]-> AST-02 -> DOC-E1#p3 -[supports]-> AST-02)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-B1#p1] (score 3.773; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[DOC-K1#p1] (score 1.839; DOC-K1#p1 -[cites]-> DOC-B1#p1)
The Corvid audit is an invented periodic examination of released summaries. At each audit sitting the auditor draws a sample of released summaries, and for every line in the sample checks that each cited passage identifier resolves to a passage in the approved corpus, that the line has a Wren ledger entry, and that the recorded Kestrel band matches the number of cited passages that actually support the line.

Sources: [DOC-B1#p2], [DOC-E1#p3], [DOC-B1#p1], [DOC-K1#p1]
```

### mode=vector

```
Question: How often is the Kestrel score recomputed?
Mode: vector

[DOC-B1#p2] (score 0.212; direct lexical match)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-H1#p3] (score 0.192; direct lexical match)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

[DOC-E1#p3] (score 0.181; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-B1#p3] (score 0.158; direct lexical match)
A line whose Kestrel score is K0 must be withheld from the released summary. In its place the renderer emits the standard abstention sentence and nothing else, so that a reader can see that a line was considered and set aside rather than silently dropped. This handling follows the fictional Harrowgate working note on unsupported lines and is not to be relaxed at desk level.

[DOC-B1#p1] (score 0.144; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

Sources: [DOC-B1#p2], [DOC-H1#p3], [DOC-E1#p3], [DOC-B1#p3], [DOC-B1#p1]
```

## Q06: What happens to a summary line with Kestrel score K0?

Answerable: True. Gold: DOC-B1#p3

### mode=lexical

```
Question: What happens to a summary line with Kestrel score K0?
Mode: lexical

[DOC-B1#p1] (score 9.268; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[DOC-B1#p3] (score 7.948; direct lexical match)
A line whose Kestrel score is K0 must be withheld from the released summary. In its place the renderer emits the standard abstention sentence and nothing else, so that a reader can see that a line was considered and set aside rather than silently dropped. This handling follows the fictional Harrowgate working note on unsupported lines and is not to be relaxed at desk level.

[DOC-E1#p3] (score 4.589; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-B1#p2] (score 4.317; direct lexical match)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-H1#p3] (score 3.324; direct lexical match)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

Sources: [DOC-B1#p1], [DOC-B1#p3], [DOC-E1#p3], [DOC-B1#p2], [DOC-H1#p3]
```

### mode=graph

```
Question: What happens to a summary line with Kestrel score K0?
Mode: graph

[DOC-B1#p1] (score 9.268; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[DOC-B1#p3] (score 7.948; direct lexical match)
A line whose Kestrel score is K0 must be withheld from the released summary. In its place the renderer emits the standard abstention sentence and nothing else, so that a reader can see that a line was considered and set aside rather than silently dropped. This handling follows the fictional Harrowgate working note on unsupported lines and is not to be relaxed at desk level.

[DOC-B1#p2] (score 5.317; DOC-E1#p3 -[supports]-> AST-02 -> DOC-B1#p2 -[supports]-> AST-02)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-E1#p3] (score 4.589; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-K1#p1] (score 2.735; DOC-K1#p1 -[cites]-> DOC-B1#p1)
The Corvid audit is an invented periodic examination of released summaries. At each audit sitting the auditor draws a sample of released summaries, and for every line in the sample checks that each cited passage identifier resolves to a passage in the approved corpus, that the line has a Wren ledger entry, and that the recorded Kestrel band matches the number of cited passages that actually support the line.

Sources: [DOC-B1#p1], [DOC-B1#p3], [DOC-B1#p2], [DOC-E1#p3], [DOC-K1#p1]
```

### mode=vector

```
Question: What happens to a summary line with Kestrel score K0?
Mode: vector

[DOC-B1#p1] (score 0.430; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[DOC-B1#p3] (score 0.387; direct lexical match)
A line whose Kestrel score is K0 must be withheld from the released summary. In its place the renderer emits the standard abstention sentence and nothing else, so that a reader can see that a line was considered and set aside rather than silently dropped. This handling follows the fictional Harrowgate working note on unsupported lines and is not to be relaxed at desk level.

[DOC-H1#p3] (score 0.314; direct lexical match)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

[DOC-E1#p1] (score 0.295; direct lexical match)
The Brindle flag is an invented marker attached to a single summary line when two approved passages make statements about that line that cannot both be true. The flag names the line, the two passage identifiers, and the reviewer who noticed the conflict. A flag is never attached to a whole summary and never to a passage; it belongs to the line whose support is in dispute.

[DOC-G1#p1] (score 0.295; direct lexical match)
The Sable checkpoint is an invented release gate that every summary passes before it leaves the fictional review workspace. The checkpoint asks two questions of every line: does the line have an entry in the Wren ledger, and does every passage identifier cited by the line resolve to a passage in the approved corpus. A summary with even one line that fails either question does not pass the checkpoint.

Sources: [DOC-B1#p1], [DOC-B1#p3], [DOC-H1#p3], [DOC-E1#p1], [DOC-G1#p1]
```

## Q07: What are the four rungs of the Thornbury ladder?

Answerable: True. Gold: DOC-C1#p1

### mode=lexical

```
Question: What are the four rungs of the Thornbury ladder?
Mode: lexical

[DOC-C1#p3] (score 5.789; direct lexical match)
A line descends the Thornbury ladder only after a Lantern review has closed the disagreement, either by upholding one of the passages or by marking both as background. The descent is written into the Wren ledger as a single entry naming the review that closed the dispute. A line that reaches rung four does not descend until the Corvid audit has reported on it.

[DOC-C1#p1] (score 5.572; direct lexical match)
The Thornbury ladder is an invented four-rung escalation path for a summary line whose supporting passages disagree with one another. On rung one the original reviewer re-reads both passages and records whether the disagreement survives a careful reading. On rung two a Brindle flag is raised against the line. On rung three the line is sent to a Lantern review by a second reviewer. On rung four the line is entered into the Corvid audit register for the next audit sitting.

[DOC-J1#p3] (score 4.199; direct lexical match)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

[DOC-D1#p1] (score 3.713; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-C1#p2] (score 3.228; direct lexical match)
A line climbs at most one rung of the Thornbury ladder per Osprey window, so that each rung has a full window in which to resolve the disagreement before the next is reached. Skipping a rung is permitted in one situation only: when the passage on the disagreeing side carries Halden tier one, the reviewer may move directly from rung one to rung three without raising a flag, because a tier-one source is treated as background rather than as evidence.

Sources: [DOC-C1#p3], [DOC-C1#p1], [DOC-J1#p3], [DOC-D1#p1], [DOC-C1#p2]
```

### mode=graph

```
Question: What are the four rungs of the Thornbury ladder?
Mode: graph

[DOC-C1#p3] (score 6.589; DOC-J1#p3 -[refines]-> DOC-C1#p3)
A line descends the Thornbury ladder only after a Lantern review has closed the disagreement, either by upholding one of the passages or by marking both as background. The descent is written into the Wren ledger as a single entry naming the review that closed the dispute. A line that reaches rung four does not descend until the Corvid audit has reported on it.

[DOC-C1#p1] (score 5.572; direct lexical match)
The Thornbury ladder is an invented four-rung escalation path for a summary line whose supporting passages disagree with one another. On rung one the original reviewer re-reads both passages and records whether the disagreement survives a careful reading. On rung two a Brindle flag is raised against the line. On rung three the line is sent to a Lantern review by a second reviewer. On rung four the line is entered into the Corvid audit register for the next audit sitting.

[DOC-J1#p3] (score 4.999; DOC-J1#p3 -[refines]-> DOC-C1#p3)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

[DOC-E1#p2] (score 1.000; DOC-J1#p3 -[supports]-> DOC-E1#p2)
Any reviewer may raise a Brindle flag, and raising one requires no approval. Only a Lantern review may clear a flag, and the person who raised the flag may not perform that review. A cleared flag is not deleted: it remains in the Wren ledger together with the closing note of the review that cleared it, so that a later reader can see both that a disagreement existed and how it was settled.

[DOC-J1#p1] (score 1.000; DOC-C1#p3 -[supports]-> DOC-J1#p1)
The Lantern review is an invented second reading of a summary line that carries a Brindle flag. It is performed by a reviewer who did not raise the flag and who did not write the line. The reviewer reads both disputed passages in full, reads the surrounding passages of each document, and writes a short finding that states which passage, if either, the line should rest on.

Sources: [DOC-C1#p3], [DOC-C1#p1], [DOC-J1#p3], [DOC-E1#p2], [DOC-J1#p1]
```

### mode=vector

```
Question: What are the four rungs of the Thornbury ladder?
Mode: vector

[DOC-C1#p3] (score 0.217; direct lexical match)
A line descends the Thornbury ladder only after a Lantern review has closed the disagreement, either by upholding one of the passages or by marking both as background. The descent is written into the Wren ledger as a single entry naming the review that closed the dispute. A line that reaches rung four does not descend until the Corvid audit has reported on it.

[DOC-C1#p1] (score 0.192; direct lexical match)
The Thornbury ladder is an invented four-rung escalation path for a summary line whose supporting passages disagree with one another. On rung one the original reviewer re-reads both passages and records whether the disagreement survives a careful reading. On rung two a Brindle flag is raised against the line. On rung three the line is sent to a Lantern review by a second reviewer. On rung four the line is entered into the Corvid audit register for the next audit sitting.

[DOC-J1#p3] (score 0.171; direct lexical match)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

[DOC-D1#p1] (score 0.147; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-E1#p3] (score 0.120; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

Sources: [DOC-C1#p3], [DOC-C1#p1], [DOC-J1#p3], [DOC-D1#p1], [DOC-E1#p3]
```

## Q08: When may a rung of the Thornbury ladder be skipped?

Answerable: True. Gold: DOC-C1#p2

### mode=lexical

```
Question: When may a rung of the Thornbury ladder be skipped?
Mode: lexical

[DOC-C1#p2] (score 7.087; direct lexical match)
A line climbs at most one rung of the Thornbury ladder per Osprey window, so that each rung has a full window in which to resolve the disagreement before the next is reached. Skipping a rung is permitted in one situation only: when the passage on the disagreeing side carries Halden tier one, the reviewer may move directly from rung one to rung three without raising a flag, because a tier-one source is treated as background rather than as evidence.

[DOC-C1#p1] (score 6.945; direct lexical match)
The Thornbury ladder is an invented four-rung escalation path for a summary line whose supporting passages disagree with one another. On rung one the original reviewer re-reads both passages and records whether the disagreement survives a careful reading. On rung two a Brindle flag is raised against the line. On rung three the line is sent to a Lantern review by a second reviewer. On rung four the line is entered into the Corvid audit register for the next audit sitting.

[DOC-C1#p3] (score 5.998; direct lexical match)
A line descends the Thornbury ladder only after a Lantern review has closed the disagreement, either by upholding one of the passages or by marking both as background. The descent is written into the Wren ledger as a single entry naming the review that closed the dispute. A line that reaches rung four does not descend until the Corvid audit has reported on it.

[DOC-D1#p1] (score 5.859; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-J1#p3] (score 4.199; direct lexical match)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

Sources: [DOC-C1#p2], [DOC-C1#p1], [DOC-C1#p3], [DOC-D1#p1], [DOC-J1#p3]
```

### mode=graph

```
Question: When may a rung of the Thornbury ladder be skipped?
Mode: graph

[DOC-C1#p2] (score 7.087; direct lexical match)
A line climbs at most one rung of the Thornbury ladder per Osprey window, so that each rung has a full window in which to resolve the disagreement before the next is reached. Skipping a rung is permitted in one situation only: when the passage on the disagreeing side carries Halden tier one, the reviewer may move directly from rung one to rung three without raising a flag, because a tier-one source is treated as background rather than as evidence.

[DOC-C1#p1] (score 6.945; direct lexical match)
The Thornbury ladder is an invented four-rung escalation path for a summary line whose supporting passages disagree with one another. On rung one the original reviewer re-reads both passages and records whether the disagreement survives a careful reading. On rung two a Brindle flag is raised against the line. On rung three the line is sent to a Lantern review by a second reviewer. On rung four the line is entered into the Corvid audit register for the next audit sitting.

[DOC-D1#p1] (score 6.659; DOC-C1#p2 -[refines]-> DOC-D1#p1)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-C1#p3] (score 5.998; direct lexical match)
A line descends the Thornbury ladder only after a Lantern review has closed the disagreement, either by upholding one of the passages or by marking both as background. The descent is written into the Wren ledger as a single entry naming the review that closed the dispute. A line that reaches rung four does not descend until the Corvid audit has reported on it.

[DOC-J1#p3] (score 4.999; DOC-J1#p3 -[refines]-> DOC-C1#p3)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

Sources: [DOC-C1#p2], [DOC-C1#p1], [DOC-D1#p1], [DOC-C1#p3], [DOC-J1#p3]
```

### mode=vector

```
Question: When may a rung of the Thornbury ladder be skipped?
Mode: vector

[DOC-C1#p1] (score 0.385; direct lexical match)
The Thornbury ladder is an invented four-rung escalation path for a summary line whose supporting passages disagree with one another. On rung one the original reviewer re-reads both passages and records whether the disagreement survives a careful reading. On rung two a Brindle flag is raised against the line. On rung three the line is sent to a Lantern review by a second reviewer. On rung four the line is entered into the Corvid audit register for the next audit sitting.

[DOC-C1#p2] (score 0.359; direct lexical match)
A line climbs at most one rung of the Thornbury ladder per Osprey window, so that each rung has a full window in which to resolve the disagreement before the next is reached. Skipping a rung is permitted in one situation only: when the passage on the disagreeing side carries Halden tier one, the reviewer may move directly from rung one to rung three without raising a flag, because a tier-one source is treated as background rather than as evidence.

[DOC-C1#p3] (score 0.289; direct lexical match)
A line descends the Thornbury ladder only after a Lantern review has closed the disagreement, either by upholding one of the passages or by marking both as background. The descent is written into the Wren ledger as a single entry naming the review that closed the dispute. A line that reaches rung four does not descend until the Corvid audit has reported on it.

[DOC-J1#p3] (score 0.257; direct lexical match)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

[DOC-D1#p1] (score 0.221; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

Sources: [DOC-C1#p1], [DOC-C1#p2], [DOC-C1#p3], [DOC-J1#p3], [DOC-D1#p1]
```

## Q09: How many Osprey windows are there in one cycle of the Ferris loop?

Answerable: True. Gold: DOC-D1#p1, DOC-I1#p2

### mode=lexical

```
Question: How many Osprey windows are there in one cycle of the Ferris loop?
Mode: lexical

[DOC-I1#p2] (score 10.701; direct lexical match)
One cycle of the Ferris loop is three Osprey windows long. The cycle boundary is the closing entry of the third window, and Kestrel recomputation and Marlow recomputation schedules are counted in these cycles. The desk does not shorten a cycle even when no notes have arrived, because the schedule of the other procedures depends on the cycle length being fixed.

[DOC-D1#p1] (score 8.826; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-I1#p1] (score 5.565; direct lexical match)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

[DOC-B1#p2] (score 5.193; direct lexical match)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-E1#p3] (score 4.804; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

Sources: [DOC-I1#p2], [DOC-D1#p1], [DOC-I1#p1], [DOC-B1#p2], [DOC-E1#p3]
```

### mode=graph

```
Question: How many Osprey windows are there in one cycle of the Ferris loop?
Mode: graph

[DOC-I1#p2] (score 11.701; DOC-I1#p2 -[supports]-> DOC-D1#p1)
One cycle of the Ferris loop is three Osprey windows long. The cycle boundary is the closing entry of the third window, and Kestrel recomputation and Marlow recomputation schedules are counted in these cycles. The desk does not shorten a cycle even when no notes have arrived, because the schedule of the other procedures depends on the cycle length being fixed.

[DOC-D1#p1] (score 9.826; DOC-I1#p2 -[supports]-> DOC-D1#p1)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-I1#p1] (score 5.565; direct lexical match)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

[DOC-I1#p3] (score 5.382; DOC-I1#p3 -[refines]-> DOC-I1#p1)
The Ferris loop closes for a summary when two consecutive cycles have passed with no notes attached to any of its lines. A closed loop is recorded in the Wren ledger with a closing entry. A note that arrives after closure reopens the loop, and the count of quiet cycles starts again from zero.

[DOC-C1#p2] (score 3.314; DOC-C1#p2 -[refines]-> DOC-D1#p1)
A line climbs at most one rung of the Thornbury ladder per Osprey window, so that each rung has a full window in which to resolve the disagreement before the next is reached. Skipping a rung is permitted in one situation only: when the passage on the disagreeing side carries Halden tier one, the reviewer may move directly from rung one to rung three without raising a flag, because a tier-one source is treated as background rather than as evidence.

Sources: [DOC-I1#p2], [DOC-D1#p1], [DOC-I1#p1], [DOC-I1#p3], [DOC-C1#p2]
```

### mode=vector

```
Question: How many Osprey windows are there in one cycle of the Ferris loop?
Mode: vector

[DOC-I1#p2] (score 0.491; direct lexical match)
One cycle of the Ferris loop is three Osprey windows long. The cycle boundary is the closing entry of the third window, and Kestrel recomputation and Marlow recomputation schedules are counted in these cycles. The desk does not shorten a cycle even when no notes have arrived, because the schedule of the other procedures depends on the cycle length being fixed.

[DOC-D1#p1] (score 0.361; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-I1#p3] (score 0.327; direct lexical match)
The Ferris loop closes for a summary when two consecutive cycles have passed with no notes attached to any of its lines. A closed loop is recorded in the Wren ledger with a closing entry. A note that arrives after closure reopens the loop, and the count of quiet cycles starts again from zero.

[DOC-C1#p2] (score 0.251; direct lexical match)
A line climbs at most one rung of the Thornbury ladder per Osprey window, so that each rung has a full window in which to resolve the disagreement before the next is reached. Skipping a rung is permitted in one situation only: when the passage on the disagreeing side carries Halden tier one, the reviewer may move directly from rung one to rung three without raising a flag, because a tier-one source is treated as background rather than as evidence.

[DOC-I1#p1] (score 0.244; direct lexical match)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

Sources: [DOC-I1#p2], [DOC-D1#p1], [DOC-I1#p3], [DOC-C1#p2], [DOC-I1#p1]
```

## Q10: What is allowed outside an Osprey window?

Answerable: True. Gold: DOC-D1#p3

### mode=lexical

```
Question: What is allowed outside an Osprey window?
Mode: lexical

[DOC-D1#p3] (score 8.742; direct lexical match)
Outside an Osprey window nothing moves in the queue or on the ladder, with one exception: a Brindle flag may be raised at any time, inside or outside a window, because a flag records a disagreement that was noticed and delaying that record would hide the disagreement. Clearing a flag, however, waits for a Lantern review and is never done outside a window.

[DOC-D1#p1] (score 3.659; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-D1#p2] (score 3.137; direct lexical match)
Inside an Osprey window the desk performs three actions in a fixed order. First, the Marlow Index of every queued request is recomputed. Second, any Kestrel bands that are due under the Ferris loop schedule are refreshed. Third, the Wren ledger is reconciled so that every line touched during the window has an entry that names the window. The window closes with a closing entry, and no further action of these three kinds is taken until the next window opens.

[DOC-F1#p2] (score 2.997; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-A1#p2] (score 2.882; direct lexical match)
The Marlow Index is recomputed for every queued request at the start of each Osprey window. Recomputation by hand between windows is permitted only when the Wren ledger shows that the request has no entry for the previous window, and any hand recomputation must itself be written into the ledger with the initials of the reviewer who performed it. A recomputation that is not in the ledger is treated as if it had not happened.

Sources: [DOC-D1#p3], [DOC-D1#p1], [DOC-D1#p2], [DOC-F1#p2], [DOC-A1#p2]
```

### mode=graph

```
Question: What is allowed outside an Osprey window?
Mode: graph

[DOC-D1#p3] (score 8.742; direct lexical match)
Outside an Osprey window nothing moves in the queue or on the ladder, with one exception: a Brindle flag may be raised at any time, inside or outside a window, because a flag records a disagreement that was noticed and delaying that record would hide the disagreement. Clearing a flag, however, waits for a Lantern review and is never done outside a window.

[DOC-F1#p2] (score 3.797; DOC-F1#p2 -[refines]-> DOC-D1#p3)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-D1#p1] (score 3.659; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-A1#p2] (score 3.382; DOC-D1#p2 -[cites]-> DOC-A1#p2)
The Marlow Index is recomputed for every queued request at the start of each Osprey window. Recomputation by hand between windows is permitted only when the Wren ledger shows that the request has no entry for the previous window, and any hand recomputation must itself be written into the ledger with the initials of the reviewer who performed it. A recomputation that is not in the ledger is treated as if it had not happened.

[DOC-I1#p2] (score 3.381; DOC-I1#p2 -[supports]-> DOC-D1#p1)
One cycle of the Ferris loop is three Osprey windows long. The cycle boundary is the closing entry of the third window, and Kestrel recomputation and Marlow recomputation schedules are counted in these cycles. The desk does not shorten a cycle even when no notes have arrived, because the schedule of the other procedures depends on the cycle length being fixed.

Sources: [DOC-D1#p3], [DOC-F1#p2], [DOC-D1#p1], [DOC-A1#p2], [DOC-I1#p2]
```

### mode=vector

```
Question: What is allowed outside an Osprey window?
Mode: vector

[DOC-D1#p3] (score 0.464; direct lexical match)
Outside an Osprey window nothing moves in the queue or on the ladder, with one exception: a Brindle flag may be raised at any time, inside or outside a window, because a flag records a disagreement that was noticed and delaying that record would hide the disagreement. Clearing a flag, however, waits for a Lantern review and is never done outside a window.

[DOC-D1#p2] (score 0.389; direct lexical match)
Inside an Osprey window the desk performs three actions in a fixed order. First, the Marlow Index of every queued request is recomputed. Second, any Kestrel bands that are due under the Ferris loop schedule are refreshed. Third, the Wren ledger is reconciled so that every line touched during the window has an entry that names the window. The window closes with a closing entry, and no further action of these three kinds is taken until the next window opens.

[DOC-D1#p1] (score 0.369; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-F1#p2] (score 0.212; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-A1#p2] (score 0.188; direct lexical match)
The Marlow Index is recomputed for every queued request at the start of each Osprey window. Recomputation by hand between windows is permitted only when the Wren ledger shows that the request has no entry for the previous window, and any hand recomputation must itself be written into the ledger with the initials of the reviewer who performed it. A recomputation that is not in the ledger is treated as if it had not happened.

Sources: [DOC-D1#p3], [DOC-D1#p2], [DOC-D1#p1], [DOC-F1#p2], [DOC-A1#p2]
```

## Q11: Who may raise a Brindle flag and who may clear it?

Answerable: True. Gold: DOC-E1#p2

### mode=lexical

```
Question: Who may raise a Brindle flag and who may clear it?
Mode: lexical

[DOC-E1#p2] (score 9.990; direct lexical match)
Any reviewer may raise a Brindle flag, and raising one requires no approval. Only a Lantern review may clear a flag, and the person who raised the flag may not perform that review. A cleared flag is not deleted: it remains in the Wren ledger together with the closing note of the review that cleared it, so that a later reader can see both that a disagreement existed and how it was settled.

[DOC-J1#p1] (score 6.356; direct lexical match)
The Lantern review is an invented second reading of a summary line that carries a Brindle flag. It is performed by a reviewer who did not raise the flag and who did not write the line. The reviewer reads both disputed passages in full, reads the surrounding passages of each document, and writes a short finding that states which passage, if either, the line should rest on.

[DOC-D1#p3] (score 3.854; direct lexical match)
Outside an Osprey window nothing moves in the queue or on the ladder, with one exception: a Brindle flag may be raised at any time, inside or outside a window, because a flag records a disagreement that was noticed and delaying that record would hide the disagreement. Clearing a flag, however, waits for a Lantern review and is never done outside a window.

[DOC-J1#p3] (score 3.771; direct lexical match)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

[DOC-E1#p1] (score 3.729; direct lexical match)
The Brindle flag is an invented marker attached to a single summary line when two approved passages make statements about that line that cannot both be true. The flag names the line, the two passage identifiers, and the reviewer who noticed the conflict. A flag is never attached to a whole summary and never to a passage; it belongs to the line whose support is in dispute.

Sources: [DOC-E1#p2], [DOC-J1#p1], [DOC-D1#p3], [DOC-J1#p3], [DOC-E1#p1]
```

### mode=graph

```
Question: Who may raise a Brindle flag and who may clear it?
Mode: graph

[DOC-E1#p2] (score 10.990; DOC-D1#p3 -[supports]-> DOC-E1#p2)
Any reviewer may raise a Brindle flag, and raising one requires no approval. Only a Lantern review may clear a flag, and the person who raised the flag may not perform that review. A cleared flag is not deleted: it remains in the Wren ledger together with the closing note of the review that cleared it, so that a later reader can see both that a disagreement existed and how it was settled.

[DOC-J1#p1] (score 6.356; direct lexical match)
The Lantern review is an invented second reading of a summary line that carries a Brindle flag. It is performed by a reviewer who did not raise the flag and who did not write the line. The reviewer reads both disputed passages in full, reads the surrounding passages of each document, and writes a short finding that states which passage, if either, the line should rest on.

[DOC-D1#p3] (score 4.854; DOC-D1#p3 -[supports]-> DOC-E1#p2)
Outside an Osprey window nothing moves in the queue or on the ladder, with one exception: a Brindle flag may be raised at any time, inside or outside a window, because a flag records a disagreement that was noticed and delaying that record would hide the disagreement. Clearing a flag, however, waits for a Lantern review and is never done outside a window.

[DOC-J1#p3] (score 4.771; DOC-J1#p3 -[supports]-> DOC-E1#p2)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

[DOC-A1#p3] (score 4.670; DOC-E1#p2 -[supports]-> AST-03 -> DOC-A1#p3 -[supports]-> AST-03)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

Sources: [DOC-E1#p2], [DOC-J1#p1], [DOC-D1#p3], [DOC-J1#p3], [DOC-A1#p3]
```

### mode=vector

```
Question: Who may raise a Brindle flag and who may clear it?
Mode: vector

[DOC-E1#p2] (score 0.460; direct lexical match)
Any reviewer may raise a Brindle flag, and raising one requires no approval. Only a Lantern review may clear a flag, and the person who raised the flag may not perform that review. A cleared flag is not deleted: it remains in the Wren ledger together with the closing note of the review that cleared it, so that a later reader can see both that a disagreement existed and how it was settled.

[DOC-D1#p3] (score 0.331; direct lexical match)
Outside an Osprey window nothing moves in the queue or on the ladder, with one exception: a Brindle flag may be raised at any time, inside or outside a window, because a flag records a disagreement that was noticed and delaying that record would hide the disagreement. Clearing a flag, however, waits for a Lantern review and is never done outside a window.

[DOC-A1#p3] (score 0.301; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-J1#p1] (score 0.286; direct lexical match)
The Lantern review is an invented second reading of a summary line that carries a Brindle flag. It is performed by a reviewer who did not raise the flag and who did not write the line. The reviewer reads both disputed passages in full, reads the surrounding passages of each document, and writes a short finding that states which passage, if either, the line should rest on.

[DOC-J1#p3] (score 0.257; direct lexical match)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

Sources: [DOC-E1#p2], [DOC-D1#p3], [DOC-A1#p3], [DOC-J1#p1], [DOC-J1#p3]
```

## Q12: Which five fields does a Quillon handoff carry?

Answerable: True. Gold: DOC-F1#p1

### mode=lexical

```
Question: Which five fields does a Quillon handoff carry?
Mode: lexical

[DOC-F1#p3] (score 12.190; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

[DOC-F1#p1] (score 9.370; direct lexical match)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

[DOC-F1#p2] (score 8.982; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-B1#p1] (score 3.938; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[DOC-L1#p3] (score 2.647; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

Sources: [DOC-F1#p3], [DOC-F1#p1], [DOC-F1#p2], [DOC-B1#p1], [DOC-L1#p3]
```

### mode=graph

```
Question: Which five fields does a Quillon handoff carry?
Mode: graph

[DOC-F1#p3] (score 12.190; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

[DOC-F1#p1] (score 9.370; direct lexical match)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

[DOC-F1#p2] (score 8.982; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-G1#p3] (score 2.971; DOC-F1#p3 -[refines]-> DOC-G1#p3)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

[DOC-D1#p3] (score 0.800; DOC-F1#p2 -[refines]-> DOC-D1#p3)
Outside an Osprey window nothing moves in the queue or on the ladder, with one exception: a Brindle flag may be raised at any time, inside or outside a window, because a flag records a disagreement that was noticed and delaying that record would hide the disagreement. Clearing a flag, however, waits for a Lantern review and is never done outside a window.

Sources: [DOC-F1#p3], [DOC-F1#p1], [DOC-F1#p2], [DOC-G1#p3], [DOC-D1#p3]
```

### mode=vector

```
Question: Which five fields does a Quillon handoff carry?
Mode: vector

[DOC-F1#p3] (score 0.454; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

[DOC-F1#p2] (score 0.379; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-F1#p1] (score 0.241; direct lexical match)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

[DOC-B1#p1] (score 0.086; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

[DOC-L1#p3] (score 0.069; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

Sources: [DOC-F1#p3], [DOC-F1#p2], [DOC-F1#p1], [DOC-B1#p1], [DOC-L1#p3]
```

## Q13: What happens when a Quillon handoff arrives with a field missing?

Answerable: True. Gold: DOC-F1#p3

### mode=lexical

```
Question: What happens when a Quillon handoff arrives with a field missing?
Mode: lexical

[DOC-F1#p3] (score 16.798; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

[DOC-F1#p2] (score 6.464; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-F1#p1] (score 4.396; direct lexical match)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

[DOC-I1#p3] (score 2.987; direct lexical match)
The Ferris loop closes for a summary when two consecutive cycles have passed with no notes attached to any of its lines. A closed loop is recorded in the Wren ledger with a closing entry. A note that arrives after closure reopens the loop, and the count of quiet cycles starts again from zero.

[DOC-G1#p3] (score 2.171; direct lexical match)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

Sources: [DOC-F1#p3], [DOC-F1#p2], [DOC-F1#p1], [DOC-I1#p3], [DOC-G1#p3]
```

### mode=graph

```
Question: What happens when a Quillon handoff arrives with a field missing?
Mode: graph

[DOC-F1#p3] (score 16.798; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

[DOC-F1#p2] (score 6.464; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-F1#p1] (score 4.396; direct lexical match)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

[DOC-G1#p3] (score 2.971; DOC-F1#p3 -[refines]-> DOC-G1#p3)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

[DOC-D1#p3] (score 0.800; DOC-F1#p2 -[refines]-> DOC-D1#p3)
Outside an Osprey window nothing moves in the queue or on the ladder, with one exception: a Brindle flag may be raised at any time, inside or outside a window, because a flag records a disagreement that was noticed and delaying that record would hide the disagreement. Clearing a flag, however, waits for a Lantern review and is never done outside a window.

Sources: [DOC-F1#p3], [DOC-F1#p2], [DOC-F1#p1], [DOC-G1#p3], [DOC-D1#p3]
```

### mode=vector

```
Question: What happens when a Quillon handoff arrives with a field missing?
Mode: vector

[DOC-F1#p3] (score 0.483; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

[DOC-F1#p2] (score 0.289; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-H1#p3] (score 0.157; direct lexical match)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

[DOC-G1#p3] (score 0.117; direct lexical match)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

[DOC-F1#p1] (score 0.110; direct lexical match)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

Sources: [DOC-F1#p3], [DOC-F1#p2], [DOC-H1#p3], [DOC-G1#p3], [DOC-F1#p1]
```

## Q14: What two questions does the Sable checkpoint ask of every line?

Answerable: True. Gold: DOC-G1#p1

### mode=lexical

```
Question: What two questions does the Sable checkpoint ask of every line?
Mode: lexical

[DOC-G1#p1] (score 11.890; direct lexical match)
The Sable checkpoint is an invented release gate that every summary passes before it leaves the fictional review workspace. The checkpoint asks two questions of every line: does the line have an entry in the Wren ledger, and does every passage identifier cited by the line resolve to a passage in the approved corpus. A summary with even one line that fails either question does not pass the checkpoint.

[DOC-G1#p2] (score 8.089; direct lexical match)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

[DOC-L1#p3] (score 5.618; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-G1#p3] (score 5.062; direct lexical match)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

[DOC-H1#p3] (score 5.022; direct lexical match)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

Sources: [DOC-G1#p1], [DOC-G1#p2], [DOC-L1#p3], [DOC-G1#p3], [DOC-H1#p3]
```

### mode=graph

```
Question: What two questions does the Sable checkpoint ask of every line?
Mode: graph

[DOC-G1#p1] (score 11.890; direct lexical match)
The Sable checkpoint is an invented release gate that every summary passes before it leaves the fictional review workspace. The checkpoint asks two questions of every line: does the line have an entry in the Wren ledger, and does every passage identifier cited by the line resolve to a passage in the approved corpus. A summary with even one line that fails either question does not pass the checkpoint.

[DOC-G1#p2] (score 9.089; DOC-L1#p3 -[supports]-> AST-04 -> DOC-G1#p2 -[supports]-> AST-04)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

[DOC-L1#p3] (score 6.618; DOC-G1#p2 -[supports]-> AST-04 -> DOC-L1#p3 -[supports]-> AST-04)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-H1#p3] (score 6.022; DOC-G1#p1 -[supports]-> AST-01 -> DOC-H1#p3 -[supports]-> AST-01)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

[DOC-L1#p1] (score 3.991; DOC-G1#p2 -[refines]-> DOC-L1#p1)
The Halden tier is an invented three-level label attached to every document in the approved corpus. Tier one is a single note that has not been read by a second reviewer. Tier two is a note that a second reviewer has read and accepted. Tier three is a note that has been read and accepted and that is cited by at least two other documents in the corpus. The tier belongs to the document, and every passage of a document carries the tier of its document.

Sources: [DOC-G1#p1], [DOC-G1#p2], [DOC-L1#p3], [DOC-H1#p3], [DOC-L1#p1]
```

### mode=vector

```
Question: What two questions does the Sable checkpoint ask of every line?
Mode: vector

[DOC-G1#p1] (score 0.637; direct lexical match)
The Sable checkpoint is an invented release gate that every summary passes before it leaves the fictional review workspace. The checkpoint asks two questions of every line: does the line have an entry in the Wren ledger, and does every passage identifier cited by the line resolve to a passage in the approved corpus. A summary with even one line that fails either question does not pass the checkpoint.

[DOC-G1#p2] (score 0.378; direct lexical match)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

[DOC-H1#p1] (score 0.336; direct lexical match)
The Wren ledger is an invented append-only record kept by the fictional review desk. For every line of every summary it stores the passage identifiers the line cites, the current Kestrel band of the line, the identifier of the Osprey window in which the entry was made, and the initials of the reviewer who made it. Entries about windows, handoffs, flags, and checkpoint results are written into the same ledger so that the whole history of a request can be read in one place.

[DOC-E1#p1] (score 0.319; direct lexical match)
The Brindle flag is an invented marker attached to a single summary line when two approved passages make statements about that line that cannot both be true. The flag names the line, the two passage identifiers, and the reviewer who noticed the conflict. A flag is never attached to a whole summary and never to a passage; it belongs to the line whose support is in dispute.

[DOC-G1#p3] (score 0.270; direct lexical match)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

Sources: [DOC-G1#p1], [DOC-G1#p2], [DOC-H1#p1], [DOC-E1#p1], [DOC-G1#p3]
```

## Q15: Which Halden tier is required for evidence passages at Sable checkpoint sign-off?

Answerable: True. Gold: DOC-G1#p2, DOC-L1#p3

### mode=lexical

```
Question: Which Halden tier is required for evidence passages at Sable checkpoint sign-off?
Mode: lexical

[DOC-G1#p2] (score 20.373; direct lexical match)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

[DOC-L1#p3] (score 19.353; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-H1#p3] (score 6.001; direct lexical match)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

[DOC-C1#p2] (score 5.902; direct lexical match)
A line climbs at most one rung of the Thornbury ladder per Osprey window, so that each rung has a full window in which to resolve the disagreement before the next is reached. Skipping a rung is permitted in one situation only: when the passage on the disagreeing side carries Halden tier one, the reviewer may move directly from rung one to rung three without raising a flag, because a tier-one source is treated as background rather than as evidence.

[DOC-L1#p1] (score 4.988; direct lexical match)
The Halden tier is an invented three-level label attached to every document in the approved corpus. Tier one is a single note that has not been read by a second reviewer. Tier two is a note that a second reviewer has read and accepted. Tier three is a note that has been read and accepted and that is cited by at least two other documents in the corpus. The tier belongs to the document, and every passage of a document carries the tier of its document.

Sources: [DOC-G1#p2], [DOC-L1#p3], [DOC-H1#p3], [DOC-C1#p2], [DOC-L1#p1]
```

### mode=graph

```
Question: Which Halden tier is required for evidence passages at Sable checkpoint sign-off?
Mode: graph

[DOC-G1#p2] (score 21.373; DOC-L1#p3 -[supports]-> AST-04 -> DOC-G1#p2 -[supports]-> AST-04)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

[DOC-L1#p3] (score 20.353; DOC-G1#p2 -[supports]-> AST-04 -> DOC-L1#p3 -[supports]-> AST-04)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-H1#p3] (score 6.001; direct lexical match)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

[DOC-L1#p1] (score 5.788; DOC-G1#p2 -[refines]-> DOC-L1#p1)
The Halden tier is an invented three-level label attached to every document in the approved corpus. Tier one is a single note that has not been read by a second reviewer. Tier two is a note that a second reviewer has read and accepted. Tier three is a note that has been read and accepted and that is cited by at least two other documents in the corpus. The tier belongs to the document, and every passage of a document carries the tier of its document.

[DOC-G1#p1] (score 5.750; DOC-H1#p3 -[supports]-> AST-01 -> DOC-G1#p1 -[supports]-> AST-01)
The Sable checkpoint is an invented release gate that every summary passes before it leaves the fictional review workspace. The checkpoint asks two questions of every line: does the line have an entry in the Wren ledger, and does every passage identifier cited by the line resolve to a passage in the approved corpus. A summary with even one line that fails either question does not pass the checkpoint.

Sources: [DOC-G1#p2], [DOC-L1#p3], [DOC-H1#p3], [DOC-L1#p1], [DOC-G1#p1]
```

### mode=vector

```
Question: Which Halden tier is required for evidence passages at Sable checkpoint sign-off?
Mode: vector

[DOC-L1#p3] (score 0.566; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-G1#p2] (score 0.542; direct lexical match)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

[DOC-L1#p1] (score 0.216; direct lexical match)
The Halden tier is an invented three-level label attached to every document in the approved corpus. Tier one is a single note that has not been read by a second reviewer. Tier two is a note that a second reviewer has read and accepted. Tier three is a note that has been read and accepted and that is cited by at least two other documents in the corpus. The tier belongs to the document, and every passage of a document carries the tier of its document.

[DOC-H1#p3] (score 0.192; direct lexical match)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

[DOC-G1#p3] (score 0.190; direct lexical match)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

Sources: [DOC-L1#p3], [DOC-G1#p2], [DOC-L1#p1], [DOC-H1#p3], [DOC-G1#p3]
```

## Q16: How is a correction made to the Wren ledger?

Answerable: True. Gold: DOC-H1#p2

### mode=lexical

```
Question: How is a correction made to the Wren ledger?
Mode: lexical

[DOC-H1#p2] (score 7.515; direct lexical match)
Entries in the Wren ledger are never edited and never removed. A correction is made by appending a new entry that names the entry it corrects and states what was wrong. A reader who follows the chain of corrections from the newest entry backwards therefore sees every state the line has been in, and a reader who finds an entry with no later correction may treat it as current.

[DOC-I1#p1] (score 4.770; direct lexical match)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

[DOC-H1#p1] (score 4.452; direct lexical match)
The Wren ledger is an invented append-only record kept by the fictional review desk. For every line of every summary it stores the passage identifiers the line cites, the current Kestrel band of the line, the identifier of the Osprey window in which the entry was made, and the initials of the reviewer who made it. Entries about windows, handoffs, flags, and checkpoint results are written into the same ledger so that the whole history of a request can be read in one place.

[DOC-F1#p2] (score 3.790; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

[DOC-A1#p2] (score 1.544; direct lexical match)
The Marlow Index is recomputed for every queued request at the start of each Osprey window. Recomputation by hand between windows is permitted only when the Wren ledger shows that the request has no entry for the previous window, and any hand recomputation must itself be written into the ledger with the initials of the reviewer who performed it. A recomputation that is not in the ledger is treated as if it had not happened.

Sources: [DOC-H1#p2], [DOC-I1#p1], [DOC-H1#p1], [DOC-F1#p2], [DOC-A1#p2]
```

### mode=graph

```
Question: How is a correction made to the Wren ledger?
Mode: graph

[DOC-H1#p2] (score 8.315; DOC-H1#p2 -[refines]-> DOC-H1#p1)
Entries in the Wren ledger are never edited and never removed. A correction is made by appending a new entry that names the entry it corrects and states what was wrong. A reader who follows the chain of corrections from the newest entry backwards therefore sees every state the line has been in, and a reader who finds an entry with no later correction may treat it as current.

[DOC-H1#p1] (score 5.252; DOC-H1#p2 -[refines]-> DOC-H1#p1)
The Wren ledger is an invented append-only record kept by the fictional review desk. For every line of every summary it stores the passage identifiers the line cites, the current Kestrel band of the line, the identifier of the Osprey window in which the entry was made, and the initials of the reviewer who made it. Entries about windows, handoffs, flags, and checkpoint results are written into the same ledger so that the whole history of a request can be read in one place.

[DOC-I1#p1] (score 4.770; direct lexical match)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

[DOC-I1#p3] (score 2.120; DOC-I1#p3 -[refines]-> DOC-I1#p1)
The Ferris loop closes for a summary when two consecutive cycles have passed with no notes attached to any of its lines. A closed loop is recorded in the Wren ledger with a closing entry. A note that arrives after closure reopens the loop, and the count of quiet cycles starts again from zero.

Sources: [DOC-H1#p2], [DOC-H1#p1], [DOC-I1#p1], [DOC-I1#p3]
```

### mode=vector

```
Question: How is a correction made to the Wren ledger?
Mode: vector

[DOC-H1#p2] (score 0.334; direct lexical match)
Entries in the Wren ledger are never edited and never removed. A correction is made by appending a new entry that names the entry it corrects and states what was wrong. A reader who follows the chain of corrections from the newest entry backwards therefore sees every state the line has been in, and a reader who finds an entry with no later correction may treat it as current.

[DOC-H1#p1] (score 0.318; direct lexical match)
The Wren ledger is an invented append-only record kept by the fictional review desk. For every line of every summary it stores the passage identifiers the line cites, the current Kestrel band of the line, the identifier of the Osprey window in which the entry was made, and the initials of the reviewer who made it. Entries about windows, handoffs, flags, and checkpoint results are written into the same ledger so that the whole history of a request can be read in one place.

[DOC-A1#p2] (score 0.250; direct lexical match)
The Marlow Index is recomputed for every queued request at the start of each Osprey window. Recomputation by hand between windows is permitted only when the Wren ledger shows that the request has no entry for the previous window, and any hand recomputation must itself be written into the ledger with the initials of the reviewer who performed it. A recomputation that is not in the ledger is treated as if it had not happened.

[DOC-I1#p1] (score 0.239; direct lexical match)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

[DOC-F1#p2] (score 0.212; direct lexical match)
A Quillon handoff is never performed during an Osprey window, because the window is the period in which indices and bands change and a handoff made while they are changing would carry stale values. The receiving reviewer countersigns the handoff in the Wren ledger before touching the request, and the countersignature names the handoff entry it accepts.

Sources: [DOC-H1#p2], [DOC-H1#p1], [DOC-A1#p2], [DOC-I1#p1], [DOC-F1#p2]
```

## Q17: When does the Ferris loop close for a summary?

Answerable: True. Gold: DOC-I1#p3

### mode=lexical

```
Question: When does the Ferris loop close for a summary?
Mode: lexical

[DOC-I1#p3] (score 5.546; direct lexical match)
The Ferris loop closes for a summary when two consecutive cycles have passed with no notes attached to any of its lines. A closed loop is recorded in the Wren ledger with a closing entry. A note that arrives after closure reopens the loop, and the count of quiet cycles starts again from zero.

[DOC-I1#p1] (score 4.158; direct lexical match)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

[DOC-B1#p2] (score 3.252; direct lexical match)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-D1#p1] (score 3.252; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-I1#p2] (score 3.252; direct lexical match)
One cycle of the Ferris loop is three Osprey windows long. The cycle boundary is the closing entry of the third window, and Kestrel recomputation and Marlow recomputation schedules are counted in these cycles. The desk does not shorten a cycle even when no notes have arrived, because the schedule of the other procedures depends on the cycle length being fixed.

Sources: [DOC-I1#p3], [DOC-I1#p1], [DOC-B1#p2], [DOC-D1#p1], [DOC-I1#p2]
```

### mode=graph

```
Question: When does the Ferris loop close for a summary?
Mode: graph

[DOC-I1#p3] (score 6.346; DOC-I1#p3 -[refines]-> DOC-I1#p1)
The Ferris loop closes for a summary when two consecutive cycles have passed with no notes attached to any of its lines. A closed loop is recorded in the Wren ledger with a closing entry. A note that arrives after closure reopens the loop, and the count of quiet cycles starts again from zero.

[DOC-I1#p1] (score 4.958; DOC-I1#p3 -[refines]-> DOC-I1#p1)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

[DOC-E1#p3] (score 4.008; DOC-B1#p2 -[supports]-> AST-02 -> DOC-E1#p3 -[supports]-> AST-02)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-B1#p2] (score 3.252; direct lexical match)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

Sources: [DOC-I1#p3], [DOC-I1#p1], [DOC-E1#p3], [DOC-B1#p2]
```

### mode=vector

```
Question: When does the Ferris loop close for a summary?
Mode: vector

[DOC-I1#p3] (score 0.400; direct lexical match)
The Ferris loop closes for a summary when two consecutive cycles have passed with no notes attached to any of its lines. A closed loop is recorded in the Wren ledger with a closing entry. A note that arrives after closure reopens the loop, and the count of quiet cycles starts again from zero.

[DOC-I1#p1] (score 0.299; direct lexical match)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

[DOC-K1#p2] (score 0.219; direct lexical match)
Any cited passage identifier that does not resolve to an approved passage causes the whole summary to be withdrawn from release. The withdrawal is appended to the Wren ledger with the unresolved identifier named, and the summary re-enters the ordered queue for rebuilding. A summary is not partially withdrawn: one unresolved citation withdraws all of it.

[DOC-D1#p1] (score 0.147; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-B1#p1] (score 0.144; direct lexical match)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

Sources: [DOC-I1#p3], [DOC-I1#p1], [DOC-K1#p2], [DOC-D1#p1], [DOC-B1#p1]
```

## Q18: Who performs a Lantern review?

Answerable: True. Gold: DOC-J1#p1

### mode=lexical

```
Question: Who performs a Lantern review?
Mode: lexical

[DOC-E1#p2] (score 3.083; direct lexical match)
Any reviewer may raise a Brindle flag, and raising one requires no approval. Only a Lantern review may clear a flag, and the person who raised the flag may not perform that review. A cleared flag is not deleted: it remains in the Wren ledger together with the closing note of the review that cleared it, so that a later reader can see both that a disagreement existed and how it was settled.

[DOC-C1#p3] (score 2.902; direct lexical match)
A line descends the Thornbury ladder only after a Lantern review has closed the disagreement, either by upholding one of the passages or by marking both as background. The descent is written into the Wren ledger as a single entry naming the review that closed the dispute. A line that reaches rung four does not descend until the Corvid audit has reported on it.

[DOC-B1#p2] (score 2.745; direct lexical match)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

[DOC-J1#p3] (score 2.728; direct lexical match)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

[DOC-L1#p2] (score 2.529; direct lexical match)
The Halden tier is assigned when a document is ingested into the approved corpus. It is raised only after a Lantern review has upheld a passage from the document against a disputed passage, or after the cross-citation count for tier three is reached at a later ingestion. A tier is never lowered except by withdrawal of the document from the corpus.

Sources: [DOC-E1#p2], [DOC-C1#p3], [DOC-B1#p2], [DOC-J1#p3], [DOC-L1#p2]
```

### mode=graph

```
Question: Who performs a Lantern review?
Mode: graph

[DOC-J1#p3] (score 3.728; DOC-J1#p3 -[supports]-> DOC-E1#p2)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

[DOC-D1#p3] (score 3.499; DOC-D1#p3 -[supports]-> DOC-E1#p2)
Outside an Osprey window nothing moves in the queue or on the ladder, with one exception: a Brindle flag may be raised at any time, inside or outside a window, because a flag records a disagreement that was noticed and delaying that record would hide the disagreement. Clearing a flag, however, waits for a Lantern review and is never done outside a window.

[DOC-J1#p1] (score 3.499; DOC-C1#p3 -[supports]-> DOC-J1#p1)
The Lantern review is an invented second reading of a summary line that carries a Brindle flag. It is performed by a reviewer who did not raise the flag and who did not write the line. The reviewer reads both disputed passages in full, reads the surrounding passages of each document, and writes a short finding that states which passage, if either, the line should rest on.

[DOC-A1#p3] (score 3.331; DOC-E1#p2 -[supports]-> AST-03 -> DOC-A1#p3 -[supports]-> AST-03)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-E1#p2] (score 3.083; direct lexical match)
Any reviewer may raise a Brindle flag, and raising one requires no approval. Only a Lantern review may clear a flag, and the person who raised the flag may not perform that review. A cleared flag is not deleted: it remains in the Wren ledger together with the closing note of the review that cleared it, so that a later reader can see both that a disagreement existed and how it was settled.

Sources: [DOC-J1#p3], [DOC-D1#p3], [DOC-J1#p1], [DOC-A1#p3], [DOC-E1#p2]
```

### mode=vector

```
Question: Who performs a Lantern review?
Mode: vector

[DOC-E1#p2] (score 0.303; direct lexical match)
Any reviewer may raise a Brindle flag, and raising one requires no approval. Only a Lantern review may clear a flag, and the person who raised the flag may not perform that review. A cleared flag is not deleted: it remains in the Wren ledger together with the closing note of the review that cleared it, so that a later reader can see both that a disagreement existed and how it was settled.

[DOC-C1#p3] (score 0.250; direct lexical match)
A line descends the Thornbury ladder only after a Lantern review has closed the disagreement, either by upholding one of the passages or by marking both as background. The descent is written into the Wren ledger as a single entry naming the review that closed the dispute. A line that reaches rung four does not descend until the Corvid audit has reported on it.

[DOC-J1#p3] (score 0.198; direct lexical match)
The finding of a Lantern review is entered in the Wren ledger and the Brindle flag on the line is cleared in the same entry. The entry names the flag it clears, the outcome chosen, and the passage upheld if there was one. The line then descends the Thornbury ladder in the next Osprey window.

[DOC-C1#p1] (score 0.167; direct lexical match)
The Thornbury ladder is an invented four-rung escalation path for a summary line whose supporting passages disagree with one another. On rung one the original reviewer re-reads both passages and records whether the disagreement survives a careful reading. On rung two a Brindle flag is raised against the line. On rung three the line is sent to a Lantern review by a second reviewer. On rung four the line is entered into the Corvid audit register for the next audit sitting.

[DOC-J1#p1] (score 0.165; direct lexical match)
The Lantern review is an invented second reading of a summary line that carries a Brindle flag. It is performed by a reviewer who did not raise the flag and who did not write the line. The reviewer reads both disputed passages in full, reads the surrounding passages of each document, and writes a short finding that states which passage, if either, the line should rest on.

Sources: [DOC-E1#p2], [DOC-C1#p3], [DOC-J1#p3], [DOC-C1#p1], [DOC-J1#p1]
```

## Q19: What does the Corvid audit do with a cited passage identifier that does not resolve?

Answerable: True. Gold: DOC-K1#p2

### mode=lexical

```
Question: What does the Corvid audit do with a cited passage identifier that does not resolve?
Mode: lexical

[DOC-K1#p1] (score 9.826; direct lexical match)
The Corvid audit is an invented periodic examination of released summaries. At each audit sitting the auditor draws a sample of released summaries, and for every line in the sample checks that each cited passage identifier resolves to a passage in the approved corpus, that the line has a Wren ledger entry, and that the recorded Kestrel band matches the number of cited passages that actually support the line.

[DOC-K1#p2] (score 8.651; direct lexical match)
Any cited passage identifier that does not resolve to an approved passage causes the whole summary to be withdrawn from release. The withdrawal is appended to the Wren ledger with the unresolved identifier named, and the summary re-enters the ordered queue for rebuilding. A summary is not partially withdrawn: one unresolved citation withdraws all of it.

[DOC-G1#p1] (score 7.069; direct lexical match)
The Sable checkpoint is an invented release gate that every summary passes before it leaves the fictional review workspace. The checkpoint asks two questions of every line: does the line have an entry in the Wren ledger, and does every passage identifier cited by the line resolve to a passage in the approved corpus. A summary with even one line that fails either question does not pass the checkpoint.

[DOC-H1#p3] (score 6.456; direct lexical match)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

[DOC-J1#p2] (score 4.912; direct lexical match)
A Lantern review has exactly three possible outcomes. The reviewer may uphold one of the two passages, in which case the line is rewritten to rest on that passage alone. The reviewer may mark both passages as background, in which case the line is withheld until a different supporting passage is found. Or the reviewer may send the line to the Corvid audit register when the disagreement cannot be settled from the approved corpus.

Sources: [DOC-K1#p1], [DOC-K1#p2], [DOC-G1#p1], [DOC-H1#p3], [DOC-J1#p2]
```

### mode=graph

```
Question: What does the Corvid audit do with a cited passage identifier that does not resolve?
Mode: graph

[DOC-K1#p1] (score 9.826; direct lexical match)
The Corvid audit is an invented periodic examination of released summaries. At each audit sitting the auditor draws a sample of released summaries, and for every line in the sample checks that each cited passage identifier resolves to a passage in the approved corpus, that the line has a Wren ledger entry, and that the recorded Kestrel band matches the number of cited passages that actually support the line.

[DOC-K1#p2] (score 9.651; DOC-K1#p2 -[supports]-> DOC-G1#p1)
Any cited passage identifier that does not resolve to an approved passage causes the whole summary to be withdrawn from release. The withdrawal is appended to the Wren ledger with the unresolved identifier named, and the summary re-enters the ordered queue for rebuilding. A summary is not partially withdrawn: one unresolved citation withdraws all of it.

[DOC-G1#p1] (score 8.069; DOC-K1#p2 -[supports]-> DOC-G1#p1)
The Sable checkpoint is an invented release gate that every summary passes before it leaves the fictional review workspace. The checkpoint asks two questions of every line: does the line have an entry in the Wren ledger, and does every passage identifier cited by the line resolve to a passage in the approved corpus. A summary with even one line that fails either question does not pass the checkpoint.

[DOC-H1#p3] (score 7.456; DOC-G1#p1 -[supports]-> AST-01 -> DOC-H1#p3 -[supports]-> AST-01)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

[DOC-B1#p1] (score 1.673; DOC-K1#p1 -[cites]-> DOC-B1#p1)
The Kestrel score is an invented five-band label, written K0 through K4, that describes how many independent approved passages agree with a single line of a draft summary. K0 means that no approved passage supports the line at all. K1 means exactly one passage supports it, K2 means two, K3 means three, and K4 means four or more passages agree. The score belongs to the line, not to the summary as a whole, so one summary can carry several different bands at once.

Sources: [DOC-K1#p1], [DOC-K1#p2], [DOC-G1#p1], [DOC-H1#p3], [DOC-B1#p1]
```

### mode=vector

```
Question: What does the Corvid audit do with a cited passage identifier that does not resolve?
Mode: vector

[DOC-K1#p1] (score 0.418; direct lexical match)
The Corvid audit is an invented periodic examination of released summaries. At each audit sitting the auditor draws a sample of released summaries, and for every line in the sample checks that each cited passage identifier resolves to a passage in the approved corpus, that the line has a Wren ledger entry, and that the recorded Kestrel band matches the number of cited passages that actually support the line.

[DOC-K1#p2] (score 0.357; direct lexical match)
Any cited passage identifier that does not resolve to an approved passage causes the whole summary to be withdrawn from release. The withdrawal is appended to the Wren ledger with the unresolved identifier named, and the summary re-enters the ordered queue for rebuilding. A summary is not partially withdrawn: one unresolved citation withdraws all of it.

[DOC-G1#p2] (score 0.255; direct lexical match)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

[DOC-G1#p1] (score 0.246; direct lexical match)
The Sable checkpoint is an invented release gate that every summary passes before it leaves the fictional review workspace. The checkpoint asks two questions of every line: does the line have an entry in the Wren ledger, and does every passage identifier cited by the line resolve to a passage in the approved corpus. A summary with even one line that fails either question does not pass the checkpoint.

[DOC-H1#p3] (score 0.236; direct lexical match)
A summary line that has no entry in the Wren ledger is not releasable, whatever its Kestrel band and whatever its cited passages say. The Sable checkpoint enforces this rule, and the Corvid audit samples released summaries to confirm that it was enforced.

Sources: [DOC-K1#p1], [DOC-K1#p2], [DOC-G1#p2], [DOC-G1#p1], [DOC-H1#p3]
```

## Q20: What are the three levels of the Halden tier?

Answerable: True. Gold: DOC-L1#p1

### mode=lexical

```
Question: What are the three levels of the Halden tier?
Mode: lexical

[DOC-L1#p1] (score 6.563; direct lexical match)
The Halden tier is an invented three-level label attached to every document in the approved corpus. Tier one is a single note that has not been read by a second reviewer. Tier two is a note that a second reviewer has read and accepted. Tier three is a note that has been read and accepted and that is cited by at least two other documents in the corpus. The tier belongs to the document, and every passage of a document carries the tier of its document.

[DOC-L1#p3] (score 6.350; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-L1#p2] (score 6.111; direct lexical match)
The Halden tier is assigned when a document is ingested into the approved corpus. It is raised only after a Lantern review has upheld a passage from the document against a disputed passage, or after the cross-citation count for tier three is reached at a later ingestion. A tier is never lowered except by withdrawal of the document from the corpus.

[DOC-C1#p2] (score 4.849; direct lexical match)
A line climbs at most one rung of the Thornbury ladder per Osprey window, so that each rung has a full window in which to resolve the disagreement before the next is reached. Skipping a rung is permitted in one situation only: when the passage on the disagreeing side carries Halden tier one, the reviewer may move directly from rung one to rung three without raising a flag, because a tier-one source is treated as background rather than as evidence.

[DOC-G1#p2] (score 4.700; direct lexical match)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

Sources: [DOC-L1#p1], [DOC-L1#p3], [DOC-L1#p2], [DOC-C1#p2], [DOC-G1#p2]
```

### mode=graph

```
Question: What are the three levels of the Halden tier?
Mode: graph

[DOC-L1#p1] (score 6.563; direct lexical match)
The Halden tier is an invented three-level label attached to every document in the approved corpus. Tier one is a single note that has not been read by a second reviewer. Tier two is a note that a second reviewer has read and accepted. Tier three is a note that has been read and accepted and that is cited by at least two other documents in the corpus. The tier belongs to the document, and every passage of a document carries the tier of its document.

[DOC-L1#p3] (score 6.350; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-L1#p2] (score 6.111; direct lexical match)
The Halden tier is assigned when a document is ingested into the approved corpus. It is raised only after a Lantern review has upheld a passage from the document against a disputed passage, or after the cross-citation count for tier three is reached at a later ingestion. A tier is never lowered except by withdrawal of the document from the corpus.

[DOC-G1#p2] (score 5.700; DOC-L1#p3 -[supports]-> AST-04 -> DOC-G1#p2 -[supports]-> AST-04)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

[DOC-A1#p1] (score 4.644; DOC-L1#p3 -[refines]-> DOC-A1#p1)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

Sources: [DOC-L1#p1], [DOC-L1#p3], [DOC-L1#p2], [DOC-G1#p2], [DOC-A1#p1]
```

### mode=vector

```
Question: What are the three levels of the Halden tier?
Mode: vector

[DOC-L1#p3] (score 0.463; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-L1#p1] (score 0.416; direct lexical match)
The Halden tier is an invented three-level label attached to every document in the approved corpus. Tier one is a single note that has not been read by a second reviewer. Tier two is a note that a second reviewer has read and accepted. Tier three is a note that has been read and accepted and that is cited by at least two other documents in the corpus. The tier belongs to the document, and every passage of a document carries the tier of its document.

[DOC-L1#p2] (score 0.328; direct lexical match)
The Halden tier is assigned when a document is ingested into the approved corpus. It is raised only after a Lantern review has upheld a passage from the document against a disputed passage, or after the cross-citation count for tier three is reached at a later ingestion. A tier is never lowered except by withdrawal of the document from the corpus.

[DOC-G1#p2] (score 0.250; direct lexical match)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

[DOC-C1#p2] (score 0.205; direct lexical match)
A line climbs at most one rung of the Thornbury ladder per Osprey window, so that each rung has a full window in which to resolve the disagreement before the next is reached. Skipping a rung is permitted in one situation only: when the passage on the disagreeing side carries Halden tier one, the reviewer may move directly from rung one to rung three without raising a flag, because a tier-one source is treated as background rather than as evidence.

Sources: [DOC-L1#p3], [DOC-L1#p1], [DOC-L1#p2], [DOC-G1#p2], [DOC-C1#p2]
```

## U01: What is the Pelican rate and how is it computed?

Answerable: False. Gold: none

### mode=lexical

```
No supporting passage found in the approved corpus.
```

### mode=graph

```
No supporting passage found in the approved corpus.
```

### mode=vector

```
No supporting passage found in the approved corpus.
```

## U02: How many seats are on the Bramble panel?

Answerable: False. Gold: none

### mode=lexical

```
No supporting passage found in the approved corpus.
```

### mode=graph

```
No supporting passage found in the approved corpus.
```

### mode=vector

```
No supporting passage found in the approved corpus.
```

## U03: What is the maximum file size accepted by the Gullwing uploader?

Answerable: False. Gold: none

### mode=lexical

```
Question: What is the maximum file size accepted by the Gullwing uploader?
Mode: lexical

[DOC-L1#p1] (score 3.178; direct lexical match)
The Halden tier is an invented three-level label attached to every document in the approved corpus. Tier one is a single note that has not been read by a second reviewer. Tier two is a note that a second reviewer has read and accepted. Tier three is a note that has been read and accepted and that is cited by at least two other documents in the corpus. The tier belongs to the document, and every passage of a document carries the tier of its document.

[DOC-F1#p3] (score 2.681; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

[DOC-I1#p1] (score 2.199; direct lexical match)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

Sources: [DOC-L1#p1], [DOC-F1#p3], [DOC-I1#p1]
```

### mode=graph

```
Question: What is the maximum file size accepted by the Gullwing uploader?
Mode: graph

[DOC-L1#p1] (score 3.178; direct lexical match)
The Halden tier is an invented three-level label attached to every document in the approved corpus. Tier one is a single note that has not been read by a second reviewer. Tier two is a note that a second reviewer has read and accepted. Tier three is a note that has been read and accepted and that is cited by at least two other documents in the corpus. The tier belongs to the document, and every passage of a document carries the tier of its document.

[DOC-F1#p3] (score 2.681; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

[DOC-I1#p1] (score 2.199; direct lexical match)
The Ferris loop is an invented correction cycle that begins when a summary is released. Readers of the released summary may attach notes to any line. At each cycle the desk reviews the notes received, decides for each note whether it identifies a genuine defect, and for every accepted note appends a correction entry to the Wren ledger. Rejected notes are also recorded, with the reason for rejection, so that a reader can see that the note was considered.

[DOC-G1#p2] (score 0.800; DOC-G1#p2 -[refines]-> DOC-L1#p1)
Sign-off at the Sable checkpoint requires that every passage cited as evidence for a line carries Halden tier two or higher. A tier-one passage may appear in a summary only as background, marked as such, and never as the evidence that supports a line. The checkpoint reviewer records the tier of every cited passage in the sign-off entry.

[DOC-G1#p3] (score 0.800; DOC-F1#p3 -[refines]-> DOC-G1#p3)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

Sources: [DOC-L1#p1], [DOC-F1#p3], [DOC-I1#p1], [DOC-G1#p2], [DOC-G1#p3]
```

### mode=vector

```
No supporting passage found in the approved corpus.
```

## U04: What colour is the Marlow Index badge printed in?

Answerable: False. Gold: none

### mode=lexical

```
Question: What colour is the Marlow Index badge printed in?
Mode: lexical

[DOC-A1#p1] (score 3.887; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-A1#p3] (score 3.769; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-F1#p3] (score 3.218; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

[DOC-L1#p3] (score 3.177; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-G1#p3] (score 2.917; direct lexical match)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

Sources: [DOC-A1#p1], [DOC-A1#p3], [DOC-F1#p3], [DOC-L1#p3], [DOC-G1#p3]
```

### mode=graph

```
Question: What colour is the Marlow Index badge printed in?
Mode: graph

[DOC-L1#p3] (score 3.977; DOC-L1#p3 -[refines]-> DOC-A1#p1)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-A1#p1] (score 3.887; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-A1#p3] (score 3.769; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-G1#p3] (score 3.717; DOC-F1#p3 -[refines]-> DOC-G1#p3)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

[DOC-F1#p1] (score 3.287; DOC-F1#p1 -[cites]-> DOC-A1#p1)
The Quillon handoff is an invented structured transfer of a partly built summary from one reviewer to another. It carries exactly five fields: the request identifier, the current Marlow Index of the request, the list of open Brindle flags against any of its lines, the identifier of the last Wren ledger entry for the request, and the name of the next Osprey window in which the receiving reviewer is expected to act.

Sources: [DOC-L1#p3], [DOC-A1#p1], [DOC-A1#p3], [DOC-G1#p3], [DOC-F1#p1]
```

### mode=vector

```
Question: What colour is the Marlow Index badge printed in?
Mode: vector

[DOC-A1#p1] (score 0.293; direct lexical match)
The Marlow Index is an invented ordering value between zero and twelve that the fictional Harrowgate review desk attaches to every summary request waiting in its queue. It is computed from three inputs: the age of the request in Osprey windows, the Halden tier of the strongest source already attached to the request, and the number of Brindle flags that remain open against it. A higher Marlow Index means the request is opened earlier in the next review sitting. The index describes queue position only and says nothing about the content of the summary.

[DOC-A1#p3] (score 0.215; direct lexical match)
The Marlow Index never overrides an open Brindle flag. A request that carries an open flag stays in the holding lane regardless of its index, and it re-enters the ordered queue only after a Lantern review has cleared the flag. Reviewers who find a high-index request in the holding lane must leave it there and note the observation in the ledger rather than moving it forward.

[DOC-L1#p3] (score 0.207; direct lexical match)
The Halden tier is one of the three inputs to the Marlow Index, and it is the input that the Sable checkpoint examines at sign-off, where evidence passages must carry tier two or higher. A reviewer who is unsure of a tier reads it from the ingestion entry in the Wren ledger rather than from memory.

[DOC-G1#p3] (score 0.192; direct lexical match)
A summary that fails the Sable checkpoint returns to the ordered queue with a ledger entry naming the failing line and the question it failed. The request keeps its Marlow Index rather than being reset, because a checkpoint failure is a defect in the summary rather than a defect in the handoff. This treatment follows the fictional Pellam committee minute on release gates.

[DOC-F1#p3] (score 0.151; direct lexical match)
A Quillon handoff that arrives with any of its five fields missing is not accepted. The request returns to the ordered queue, its Marlow Index is reset to zero, and a ledger entry records that a handoff was refused and which field was absent. The sending reviewer may resend a complete handoff in the next window.

Sources: [DOC-A1#p1], [DOC-A1#p3], [DOC-L1#p3], [DOC-G1#p3], [DOC-F1#p3]
```

## U05: Which staffing roster covers overnight desk duty?

Answerable: False. Gold: none

### mode=lexical

```
Question: Which staffing roster covers overnight desk duty?
Mode: lexical

[DOC-D1#p1] (score 4.650; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-E1#p3] (score 1.861; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-K1#p3] (score 1.452; direct lexical match)
The auditor writes a short audit note after each sitting. The note reports the number of summaries sampled, the number withdrawn, and the list of unresolved identifiers found, and it is sent to the fictional Pellam committee. The note follows the fictional Orrin desk memorandum on audit reporting and is itself entered in the ledger.

[DOC-B1#p3] (score 1.385; direct lexical match)
A line whose Kestrel score is K0 must be withheld from the released summary. In its place the renderer emits the standard abstention sentence and nothing else, so that a reader can see that a line was considered and set aside rather than silently dropped. This handling follows the fictional Harrowgate working note on unsupported lines and is not to be relaxed at desk level.

[DOC-I1#p2] (score 1.385; direct lexical match)
One cycle of the Ferris loop is three Osprey windows long. The cycle boundary is the closing entry of the third window, and Kestrel recomputation and Marlow recomputation schedules are counted in these cycles. The desk does not shorten a cycle even when no notes have arrived, because the schedule of the other procedures depends on the cycle length being fixed.

Sources: [DOC-D1#p1], [DOC-E1#p3], [DOC-K1#p3], [DOC-B1#p3], [DOC-I1#p2]
```

### mode=graph

```
Question: Which staffing roster covers overnight desk duty?
Mode: graph

[DOC-D1#p1] (score 4.650; direct lexical match)
The Osprey window is an invented recurring period during which the fictional review desk is permitted to move requests, recompute indices, and change the rung of a line on the Thornbury ladder. There are three Osprey windows in every cycle of the Ferris loop, and each window is announced in the Wren ledger by a single opening entry that names the window and the reviewer on duty for it.

[DOC-I1#p2] (score 2.385; DOC-I1#p2 -[supports]-> DOC-D1#p1)
One cycle of the Ferris loop is three Osprey windows long. The cycle boundary is the closing entry of the third window, and Kestrel recomputation and Marlow recomputation schedules are counted in these cycles. The desk does not shorten a cycle even when no notes have arrived, because the schedule of the other procedures depends on the cycle length being fixed.

[DOC-E1#p3] (score 1.861; direct lexical match)
The Brindle desk refreshes the Kestrel band of every flagged line every six cycles of the Ferris loop rather than every four, on the reasoning that a flagged line changes support more slowly while its dispute is open. This schedule is recorded here as the desk practice and is known to differ from the handling note for the Kestrel score, which states a four-cycle interval; the difference is itself an open item.

[DOC-K1#p3] (score 1.452; direct lexical match)
The auditor writes a short audit note after each sitting. The note reports the number of summaries sampled, the number withdrawn, and the list of unresolved identifiers found, and it is sent to the fictional Pellam committee. The note follows the fictional Orrin desk memorandum on audit reporting and is itself entered in the ledger.

[DOC-B1#p2] (score 1.000; DOC-E1#p3 -[supports]-> AST-02 -> DOC-B1#p2 -[supports]-> AST-02)
The Kestrel score of every line is recomputed every four cycles of the Ferris loop. The reviewer who performs the recomputation records the resulting band in the Wren ledger next to the line identifier, together with the passage identifiers that were counted. A band recorded without its passage identifiers is incomplete and must be re-entered before the next cycle closes.

Sources: [DOC-D1#p1], [DOC-I1#p2], [DOC-E1#p3], [DOC-K1#p3], [DOC-B1#p2]
```

### mode=vector

```
No supporting passage found in the approved corpus.
```
