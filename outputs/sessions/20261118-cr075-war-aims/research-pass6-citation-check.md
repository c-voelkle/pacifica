# CR-075 research, pass 6: the page references checked

18 November 2026. Scope: every citation by short key (ELL, WAITE, RICH, SHER, HUNT, ROS, JONES, KUYK, LAV, WILL, THOM, JOH) in `book-agent/revision/CR-075-outline.md` (91) and in the five files of `research-notes/` (167): 258 in all.

## Method
1. **Keyword test.** For each citation, the names and numbers in the claim before it were looked up in the cited pages of the extracted text (with one page of tolerance either side, for passages that run over). Quotes in the claim were checked verbatim.
2. **Passage test.** The claim's content words were compared with the closest 90-word passage on the cited pages; the twenty-two lowest scores were read by hand.
3. **Quote test.** Every quoted string in the notes was counted; source quotes must be under fifteen words.

## Results
- **Keyword test:** 19 of 258 flagged. All 19 were read against the page and are correct: the flags came from paraphrase ("Southern-born" for the source's "Southern born", "the Picos" for "Pico"), from quotes shortened with an ellipsis, and from claims whose names fall outside the regex.
- **Passage test:** the twelve scores below 0.3 are table rows, where the neighbouring cells dilute the claim; each cited page holds the claim.
- **One error:** the quotation of Scott's 1860 letter spelled "seigniorage"; Ellison has "seignorage" (ELL 182). Corrected in `E-california.md`.
- **Quote length:** five source quotes in the notes ran to fourteen words or more (Nesmith via JOH 186; Sherman, SHER 106 and 120; Beale's epigraph, THOM 125; Williams on Broderick, WILL 14). All five are now paraphrased or cut to a short phrase. The longer quoted strings left in the outline are canon's own text, the author's words or the drafter's schoolbook candidates, not quotations from the sources.

## Not covered
- The tests confirm that the cited page contains the claim; they do not judge whether the claim is the best reading of the source. The close reading of pass 2 is the basis for that.
- Jones is cited by chapter; within a chapter the passages are located by segment in `research-notes/F-hawaii.md`.
