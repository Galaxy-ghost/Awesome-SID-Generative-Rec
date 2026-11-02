# POI and Local-Life Papers

16 papers target POI, local-life, or spatial recommendation. Bold marks the stage each paper mainly changes.

| Paper | Venue | Problem × Stage | Pipeline |
| :-- | :-- | :-- | :-- |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr+Geo+CF` → **`RQ-VAE`** → `Dec-Only` → `Fixed / NTP` → `–` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr+Geo+CF` → **`KG-RQ`** → `Dec-Only` → `Fixed / Multi-task NTP` → `–` |
| [OneLoc](../papers/oneloc.md) | arXiv’25 | I × Representation | **`Text+Img+Geo†`** → `R-KM` → `Enc-Dec` → `Fixed / NTP → DPO` → `Beam` |
| [QT-Mob](../papers/qt-mob.md) | KDD’25 | I × Tokenization | `Text+Geo` → **`RQ-VAE`** → `Dec-Only` → `Fixed / Multi-task NTP` → `C-Beam` |
| [Spacetime-GR](../papers/spacetime-gr.md) | arXiv’25 | I × Backbone | `Geo` → `Geo-Idx` → **`Dec-Only`** → `Fixed / NTP → DPO` → `Beam` |
| [AWARE](../papers/aware.md) | arXiv’26 | VI × Training | `Text+Geo` → `Geo-Prefix+HClus` → `Dec-Only` → **`Fixed / NTP`** → `–` |
| [DOS](../papers/dos.md) | WWW’26 Short | III × Tokenization | `Text+CF` → **`Orth. RQ`** → `Dec-Only†` → `Fixed† / NTP` → `–` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | **`Text+Geo+CF`** → `R-KM+EM` → `Dec-Only` → `Altern.† / Multi-task NTP` → `Beam` |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II × Tokenization | `Text+Img+Geo+CF` → **`Contr. RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `–` |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I × Representation | **`Text+Attr+Geo`** → `R-KM` → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [LGRID](../papers/lgrid.md) | arXiv’26 | I × Representation | **`Text+Geo`** → `DSRQ` → `Disc.` → `Fixed / Discrim.` → `Scoring` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | **`Text+Geo+CF`** → `Geo-Idx+RQ` → `Disc. / Enc-Dec` → `Fixed / Discrim. / NTP` → `Scoring / Beam†` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I × Tokenization | `Text+Geo` → **`R-KM+Geo-CB`** → `Dec-Only` → `Fixed / NTP` → `Beam+Geo-Filter` |
| [ROS](../papers/ros.md) | ACL’26 | I × Tokenization | `Text+Geo` → **`Geo-Prefix+RQ-VAE`** → `Dec-Only` → `Fixed / NTP → RL` → `CoT+C-Beam` |
| [SPAR](../papers/spar.md) | arXiv’26 | I × Representation | **`Text+Geo`** → `R-KM` → `Dec-Only` → `Fixed / Multi-task NTP` → `–` |
| [Think2Go](../papers/think2go.md) | KDD’26 | III × Training | `Attr+Geo+CF†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+Beam` |
