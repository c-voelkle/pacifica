"""Map the 584 items of Pacifica_CR059-068_model_events.xlsx onto the register.

Pass 1 (automatic): the item's CR and the decision IDs in its "CR ID / lines" column, looked up
in crosswalk.csv; canon tensions through CT below. Pass 2: the manual readings in OVERRIDE,
for items whose IDs land in a no-model bucket or that cite no ID the crosswalk knows.
Usage: python3 map_events.py <events.csv>   (the workbook's Events sheet saved as CSV)
Writes events_mapped.csv beside this script.
"""
import csv, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
xw = {}
for r in csv.DictReader(open(HERE / "crosswalk.csv")):
    rid = r["row_id"]
    xw[(r["cr"], rid)] = r["register"]
    xw.setdefault((r["cr"], rid.split("_")[0]), r["register"])

CT = {
    "CR-059": {"CT2": "P01c", "CT3": "L03a", "CT5": "L06", "CT7": "N03", "CT9": "P01d", "CT10": "P04", "CT11": "P01e",
               "CT12": "L10", "CT13": "L15", "CT14": "Z59", "CT1": "Z59", "CT4": "P05", "CT6": "P05", "CT8": "Z59", "CT15": "Z59"},
    "CR-060": {"CT1": "P01e", "CT2": "P01d", "CT3": "G10", "CT4": "L03b", "CT5": "L08b", "CT6": "Z60", "CT7": "L16",
               "CT8": "L03b", "CT9": "Z60"},
    "CR-061": {"CT1": "P01g", "CT2": "L03c", "CT3": "L08c", "CT4": "L09", "CT5": "L01", "CT6": "L15", "CT7": "L08c",
               "CT8": "L08c", "CT9": "Z61"},
    "CR-062": {"CT1": "Z62", "CT2": "L01m", "CT3": "Z62", "CT4": "Z62", "CT5": "F04", "CT6": "L06", "CT7": "Z62",
               "CT8": "Z62", "CT9": "L13"},
    "CR-063": {"CT5": "L01m", "CT6": "L01", "CT8": "P04", "CT13": "P04"},
    "CR-064": {"CT1": "P04", "CT2": "P04", "CT5": "P04"},
    "CR-065": {"CT4": "P01d", "CT5": "P04"},
    "CR-068": {"CT26": "F01", "CT21": "L01", "CT28": "L01", "CT4": "Z68", "CT16": "Z68"},
}
TOK = re.compile(r"\b(N-[A-I]|CT\d+|PP\d+[a-c]?|TL\d+|AG\d|CH\d+|CO\d|MD\d|D4a|W11a|C0a|K8a|G\d+[ab]?|B\d+[ab]?|[A-Z]\d+[a-z]?)\b")

# Pass 2: manual readings (xlsx row number -> register row), filled after reading each item
OVERRIDE = {184: "X03", 314: "X04", 563: "F06", 578: "F07", 579: "F07", 581: "F07", 325: "L11", 439: "M09", 55: "F16", 57: "F16", 20: "B01", 110: "L03a", 51: "P01d", 38: 'P01a', 40: 'P01a', 41: 'X05', 48: 'X05', 50: 'P06', 67: 'G12', 68: 'G12', 79: 'L03', 81: 'F12', 120: 'L03a', 132: 'L03b', 230: 'P07', 231: 'P01c', 234: 'P10', 235: 'F12', 238: 'M11', 239: 'G02', 241: 'L03b', 315: 'X05', 317: 'G12', 321: 'M11', 328: 'X05', 329: 'X05', 405: 'F02', 406: 'M12', 410: 'M13', 412: 'P01i', 413: 'C01', 479: 'G12', 482: 'P02', 485: 'P08', 493: 'P08', 507: 'F04', 508: 'P06', 510: 'G11', 547: 'C01', 557: 'P07', 569: 'C01', 571: 'C01', 572: 'C01', 574: 'C01', 575: 'C01', 21: 'Z61', 52: 'P01g', 54: 'L03c', 82: 'P04', 83: 'L01', 138: 'G14', 139: 'G06', 140: 'G04', 141: 'L03c', 149: 'P03', 151: 'L03c', 152: 'L03c', 157: 'P01g', 158: 'P01g', 161: 'L03c', 163: 'L03c', 165: 'G06', 169: 'Z61', 170: 'L03c', 171: 'L03c', 255: 'G06', 256: 'G06', 258: 'P07', 262: 'Z61', 272: 'P07', 330: 'X03', 421: 'G07', 430: 'G01', 431: 'P01', 432: 'P01i', 433: 'P01b', 438: 'Z62', 440: 'P10', 441: 'C01', 443: 'P01', 444: 'L03', 497: 'P01', 498: 'P01e', 500: 'Z62', 501: 'P01a', 502: 'F05', 503: 'G08', 517: 'F05', 518: 'G01', 520: 'G08', 523: 'F04', 526: 'M03', 530: 'L05', 532: 'M16', 535: 'F05', 537: 'L04', 538: 'P01h', 539: 'F05', 552: 'F09', 558: 'P07', 559: 'F05', 570: 'C01', 582: 'Y01', 2: 'B01', 10: 'B01', 11: 'B01', 12: 'B01', 13: 'B01', 14: 'B01', 16: 'B01', 19: 'B01', 22: 'X05', 23: 'B01', 29: 'M14', 30: 'B01', 33: 'P01a', 34: 'M14', 36: 'M14', 37: 'Z67', 56: 'M14', 86: 'G08', 87: 'L03a', 88: 'P04', 90: 'L03a', 91: 'F18', 92: 'B01', 94: 'F02', 177: 'L03d', 193: 'P04', 194: 'X03', 195: 'X03', 196: 'G11', 197: 'G11', 199: 'P04', 200: 'Z64', 201: 'G11', 202: 'P04', 204: 'P04', 205: 'P04', 206: 'P04', 211: 'L03a', 212: 'Z67', 216: 'Z67', 276: 'P04', 278: 'L01m', 285: 'G07', 287: 'P04', 289: 'G11', 291: 'Z65', 292: 'P03', 293: 'L03b', 332: 'L01m', 335: 'L01m', 338: 'G11', 339: 'G11', 340: 'P04', 343: 'G11', 345: 'G11', 347: 'P04', 349: 'P04', 352: 'G11', 353: 'G11', 355: 'G11', 358: 'Z64', 361: 'X03', 362: 'P04', 368: 'P04', 369: 'P04', 370: 'G01', 371: 'P04', 372: 'Z65', 374: 'P04', 376: 'Z65', 379: 'G01', 380: 'P04', 381: 'Z65', 382: 'P04', 384: 'Z65', 386: 'Z67', 451: 'P04', 452: 'P04', 454: 'Z65', 455: 'P04', 456: 'L03a', 457: 'F02', 458: 'Z65', 459: 'F02', 541: 'Z64', 553: 'Y01', 555: 'Y01', 573: 'Y01', 585: 'M14', 4: 'G01', 7: 'X05', 8: 'M10', 17: 'P02', 25: 'X05', 35: 'B01', 44: 'P01a', 58: 'F12', 101: 'G01', 102: 'F17', 103: 'F02', 104: 'M04', 105: 'L02', 106: 'N02', 108: 'G01', 109: 'F18', 112: 'G01', 113: 'F02', 114: 'G01', 115: 'L02', 116: 'L03a', 217: 'G01', 218: 'F10', 221: 'G01', 223: 'G06', 224: 'F10', 225: 'X05', 226: 'P04', 295: 'P02', 296: 'G01', 299: 'L08b', 300: 'P01e', 301: 'F04', 302: 'F12', 303: 'P10', 304: 'P03', 305: 'G01', 307: 'P07', 308: 'L12', 310: 'L02', 311: 'G02', 312: 'F04', 313: 'P10', 387: 'F18', 388: 'L03b', 389: 'G09', 390: 'P09', 391: 'Z68', 392: 'L03', 393: 'L01', 394: 'G09', 395: 'L03a', 396: 'Z68', 397: 'Z68', 398: 'F18', 399: 'F12', 400: 'Z68', 401: 'P09', 402: 'G09', 403: 'G01', 404: 'L03a', 460: 'F02', 461: 'L01', 462: 'G01', 463: 'M15', 464: 'F04', 465: 'F19', 466: 'F02', 467: 'F04', 468: 'L08c', 469: 'G09', 470: 'P03', 471: 'M16', 472: 'L01', 473: 'F04', 474: 'F02', 475: 'F19', 505: 'P01a', 506: 'P01a', 543: 'M13', 546: 'L13', 549: 'G08', 550: 'G08', 561: 'P07', 562: 'F08', 564: 'P07', 565: 'Y01', 566: 'Y01', 567: 'Y01', 577: 'Y01', 580: 'Y01'}

def norm_cr(c):
    return "CR-068" if c.startswith("CR-068") else c

def auto(cr, ref):
    hits = []
    for t in TOK.findall(ref or ""):
        if t.startswith("CT"):
            d = CT.get(cr, {}).get(t)
        else:
            d = xw.get((cr, t))
        if d:
            hits.append(d)
    if not hits:
        return None, "no ID found"
    model = [h for h in hits if not h.startswith(("Z", "X"))]
    return (model[0] if model else hits[0]), ("" if len(set(hits)) == 1 else "several: " + " ".join(dict.fromkeys(hits)))

def main(src):
    out = []
    for n, r in enumerate(csv.DictReader(open(src)), start=2):
        cr = norm_cr(r["CR"])
        dest, why = auto(cr, r["CR ID / lines"])
        how = "auto"
        if n in OVERRIDE:
            dest, how = OVERRIDE[n], "manual"
        out.append(dict(xlsx_row=n, cr=r["CR"], ref=r["CR ID / lines"], register=dest or "", how=how, note=why,
                        FIN=r["FIN"], POP=r["POP"], LOG=r["LOG"], ENE=r["ENE"], event=r["Event"][:200],
                        impact=r["Impact on models"][:200]))
    with open(HERE / "events_mapped.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader(); w.writerows(out)
    return out

if __name__ == "__main__":
    o = main(sys.argv[1])
    from collections import Counter
    print(len(o), Counter("unmapped" if not x["register"] else ("Z/X" if x["register"][0] in "ZX" else "model") for x in o))
