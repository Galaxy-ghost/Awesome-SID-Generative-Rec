# Papers by Domain

[← README](../../README.md#where-to-start) · English | [中文](../zh/index/domain.md)

Papers grouped by the business domain of their evaluation datasets (multi-domain papers appear in each matching section).

Click any domain below to jump to its paper table:

| Category | Domains |
| :--- | :--- |
| **Commerce & Local** | [E-commerce (142)](#e-commerce) · [POI / Local (44)](#poi--local) · [Food / Recipe (1)](#food--recipe) · [Travel / Hotel (1)](#travel--hotel) |
| **Video & Entertainment** | [Short video / Live (21)](#short-video--live) · [Movie (12)](#movie) · [Music (10)](#music) · [Games (5)](#games) · [Long video (3)](#long-video) · [Podcast (1)](#podcast) · [Video (1)](#video) |
| **News, Reading & Visual** | [News (6)](#news) · [Book (5)](#book) · [Image / Article (3)](#image--article) |
| **Platform Services & Other** | [Ads (17)](#ads) · [Search (10)](#search) · [Apps (1)](#apps) · [Recruitment (1)](#recruitment) · [unknown (industrial) (6)](#unknown-industrial) |

## E-commerce

> 142 papers. E-commerce product recommendation (including all Amazon review subsets, Taobao, JD, etc.).

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [CID](../papers/cid.md) | SIGIR-AP’23 | II × Tokenization | `E-commerce` · `POI / Local` | `CF` |
| [TIGER](../papers/tiger.md) | NeurIPS’23 | Paradigms, Systems and Benchmarks | `E-commerce` | `Text` |
| [VQ-Rec](../papers/vq-rec.md) | WWW’23 | VI × Tokenization | `E-commerce` | `Text` |
| [ColaRec](../papers/colarec.md) | CIKM’24 | I × Backbone | `E-commerce` · `Food / Recipe` | `CF` |
| [CoST](../papers/cost.md) | RecSys’24 | I × Tokenization | `News` · `E-commerce` | `Text` |
| [EAGER](../papers/eager.md) | KDD’24 | I × Backbone | `E-commerce` · `POI / Local` | semantic: `Text` · behavior: `CF` |
| [IDGenRec](../papers/idgenrec.md) | SIGIR’24 | III × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [LC-Rec](../papers/lc-rec.md) | ICDE’24 | III × Training | `E-commerce` | `Text` |
| [LETTER](../papers/letter.md) | CIKM’24 | I × Tokenization | `E-commerce` · `POI / Local` | `Text` + `CF` |
| [LIGER](../papers/liger.md) | arXiv’24 | VI × Inference | `E-commerce` · `Games` | `Text` |
| [LMIndexer](../papers/lmindexer.md) | ICML’24 | I × Tokenization | `E-commerce` · `Search` | `Text` |
| [MBGen](../papers/mbgen.md) | CIKM’24 | I × Training | `E-commerce` | `CF` |
| [Molar](../papers/molar.md) | arXiv’24 | I × Representation | `E-commerce` · `Movie` · `Short video / Live` | `n/a` |
| [SEATER](../papers/seater.md) | SIGIR-AP’24 | V × Tokenization | `POI / Local` · `E-commerce` · `News` · `Short video / Live` | `CF` |
| [SIIT](../papers/siit.md) | arXiv’24 | III × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [TransRec](../papers/transrec.md) | KDD’24 | II × Tokenization | `E-commerce` · `POI / Local` | id: – · title: `Text` · attribute: `Text` |
| [ActionPiece](../papers/actionpiece.md) | ICML’25 | I × Tokenization | `E-commerce` | `Text` |
| [ADC-SID](../papers/adc-sid.md) | arXiv’25 | I × Tokenization | `E-commerce` · `Ads` | `Text` + `Img` + `CF` |
| [AtSpeed](../papers/atspeed.md) | ICLR’25 | V × Inference | `E-commerce` · `Movie` · `Book` | `Text` |
| [COBRA](../papers/cobra.md) | NeurIPS’25 | I × Backbone | `E-commerce` · `Ads` | `Text` |
| [DiscRec](../papers/discrec.md) | arXiv’25 | I × Backbone | `E-commerce` | A: `Text` · B: `Text` + `CF` |
| [EAGER-LLM](../papers/eager-llm.md) | WWW’25 | I × Tokenization | `E-commerce` | semantic: `Text` · behavior: `CF` |
| [ETEGRec](../papers/etegrec.md) | SIGIR’25 | III × Training | `E-commerce` | `CF` |
| [FlexCode](../papers/flexcode.md) | arXiv’25 | I × Tokenization | `E-commerce` · `Short video / Live` · `unknown (industrial)` | semantic: `Text` + `CF` · collaborative: `CF` |
| [FORGE](../papers/forge.md) | KDD’26 | Paradigms, Systems and Benchmarks | `E-commerce` · `Search` | `Text` + `Img` + `CF` |
| [GenSAR](../papers/gensar.md) | RecSys’25 | I × Tokenization | `E-commerce` · `Search` | semantic: `Text` + `CF` · collaborative: `Text` + `CF` |
| [GMC](../papers/gmc.md) | arXiv’25 | VI × Tokenization | `E-commerce` | `Text` |
| [GRAM](../papers/gram.md) | ACL’25 | I × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [GREAM](../papers/gream.md) | arXiv’25 | III × Training | `E-commerce` | `Text` |
| [GRID](../papers/grid.md) | CIKM’25 | Paradigms, Systems and Benchmarks | `E-commerce` | `Text` |
| [HiD-VAE](../papers/hid-vae.md) | arXiv’25 | II × Tokenization | `E-commerce` · `Short video / Live` | `Text` + `Attr` |
| [LLaDA-Rec](../papers/llada-rec.md) | arXiv’25 | III × Backbone | `E-commerce` | `Text` |
| [MiniOneRec](../papers/minionerec.md) | arXiv’25 | Paradigms, Systems and Benchmarks | `E-commerce` | `Text` |
| [MME-SID](../papers/mme-sid.md) | CIKM’25 | I × Tokenization | `E-commerce` | collaborative: `CF` · text: `Text` · visual: `Img` |
| [MQL4GRec](../papers/mql4grec.md) | ICLR’25 | I × Tokenization | `E-commerce` | text: `Text` · image: `Img` |
| [OneRec-Think](../papers/onerec-think.md) | arXiv’25 | III × Training | `E-commerce` · `Short video / Live` | `MM` + `CF` |
| [PSI](../papers/psi.md) | arXiv’25 | II × Tokenization | `E-commerce` · `Search` | `Text` |
| [PSRQ](../papers/psrq.md) | CIKM’25 | I × Tokenization | `E-commerce` · `Music` | text: `Text` · image: `Img` · audio: `Audio` · joint_Amazon: `Text` + `Img` · joint_Music: `Text` + `Audio` |
| [Q-BERT4Rec](../papers/q-bert4rec.md) | arXiv’25 | I × Representation | `E-commerce` | `Text` + `Img` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `News` · `Movie` · `Short video / Live` · `Book` · `POI / Local` · `Games` · `E-commerce` · `Travel / Hotel` | `Text` |
| [RPG](../papers/rpg.md) | KDD’25 | V × Backbone | `E-commerce` | `Text` |
| [SemConv](../papers/semconv.md) | AAAI’25 | III × Tokenization | `E-commerce` | `Text` + `CF` |
| [TokenRec](../papers/tokenrec.md) | TKDE’25 | I × Tokenization | `Music` · `Movie` · `E-commerce` | `CF` |
| [UNGER](../papers/unger.md) | TOIS’25 | I × Representation | `E-commerce` | `Text` + `CF` |
| [UTGRec](../papers/utgrec.md) | arXiv’25 | VI × Tokenization | `E-commerce` | `Text` + `Img` + `CF` |
| [ACERec](../papers/acerec.md) | arXiv’26 | V × Backbone | `E-commerce` | `Text` |
| [AdaSID](../papers/adasid.md) | arXiv’26 | II × Tokenization | `E-commerce` | `Text` + `Img` + `CF` |
| [Align3GR](../papers/align3gr.md) | AAAI’26 | III × Tokenization | `E-commerce` · `POI / Local` · `Ads` | `Text` + `CF` |
| [APAO](../papers/apao.md) | KDD’26 | IV × Training | `E-commerce` · `POI / Local` | `Text` |
| [API](../papers/api.md) | arXiv’26 | II × Tokenization | `E-commerce` | `Text` |
| [CAPE](../papers/cape.md) | arXiv’26 | I × Inference | `E-commerce` · `Music` | `Text` |
| [CapsID](../papers/capsid.md) | arXiv’26 | I × Tokenization | `E-commerce` · `unknown (industrial)` | A: `unknown` · B: `Text` + `Img` + `CF` |
| [CARD](../papers/card.md) | arXiv’26 | II × Tokenization | `E-commerce` | `Text` + `Img` + `CF` |
| [ChronoID](../papers/chronoid.md) | arXiv’26 | I × Tokenization | `E-commerce` | `Text` + `Time` |
| [CITE](../papers/cite.md) | Electronics’26 | I × Inference | `E-commerce` · `POI / Local` | `Text` |
| [CMRec](../papers/cmrec.md) | CIKM’26 Short | VI × Training | `Ads` · `E-commerce` | `Text` + `Img` + `CF` |
| [CogRec](../papers/cogrec.md) | arXiv’26 | III × Tokenization | `E-commerce` | `Text` |
| [DACT](../papers/dact.md) | SIGIR’26 | VI × Tokenization | `E-commerce` | `Text` + `CF` |
| [DASO](../papers/daso.md) | arXiv’26 | IV × Training | `E-commerce` · `unknown (industrial)` | `Text` + `unknown` |
| [Deco](../papers/deco.md) | arXiv’26 | V × Backbone | `E-commerce` · `Movie` · `Music` | A: `Text` · B: `unknown` |
| [DECOR](../papers/decor.md) | SIGIR’26 | III × Backbone | `E-commerce` | `Text` |
| [DIGER](../papers/diger.md) | SIGIR’26 | II × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [DiGR](../papers/digr.md) | arXiv’26 | IV × Backbone | `E-commerce` | `unknown` |
| [DPE-Rec](../papers/dpe-rec.md) | arXiv’26 | IV × Training | `Music` · `E-commerce` | A: `unknown` · B: `Text` + `Img` |
| [DREAM](../papers/dream.md) | arXiv’26 | VI × Tokenization | `E-commerce` | `Text` + `CF` |
| [Dynamic-Single-Codebook](../papers/dynamic-single-codebook.md) | arXiv’26 | V × Tokenization | `E-commerce` · `Short video / Live` · `unknown (industrial)` | `unknown` |
| [Evo-Rec](../papers/evo-rec.md) | arXiv’26 | III × Training | `E-commerce` | `Text` |
| [FedCGR](../papers/fedcgr.md) | CIKM’26 | VI × Backbone | `E-commerce` | `Text` |
| [FLASH](../papers/flash.md) | NeurIPS’26 | III × Backbone | `E-commerce` | `Text` |
| [GEM-Rec](../papers/gem-rec.md) | arXiv’26 | IV × Training | `Games` · `E-commerce` · `Ads` | `Text` |
| [GenCDR](../papers/gencdr.md) | AAAI’26 | VI × Tokenization | `E-commerce` · `Book` · `Movie` | `Text` + `unknown` |
| [GenRec-JD](../papers/genrec-jd.md) | SIGIR’26 | IV × Training | `E-commerce` | `Text` + `Img` + `CF` |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV × Training | `POI / Local` · `E-commerce` · `Ads` · `Search` | A: `Text` · B: `Text` + `CF` |
| [Ghost](../papers/ghost.md) | NeurIPS’26 | IV × Training | `E-commerce` | `Text` |
| [GR-Generalize](../papers/gr-generalize.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `E-commerce` · `Games` · `POI / Local` | `Text` |
| [GRC](../papers/grc.md) | CIKM’26 | III × Inference | `E-commerce` · `Ads` | `Text` |
| [GrIS (RecDMoN / RQ-GAE)](../papers/gris-recdmon-rq-gae.md) | CIKM’26 | I × Tokenization | `E-commerce` · `News` · `POI / Local` | `Text` + `CF` |
| [GRLM](../papers/grlm.md) | arXiv’26 | III × Tokenization | `E-commerce` | `Text` |
| [GTI](../papers/gti.md) | arXiv’26 | III × Training | `Recruitment` · `E-commerce` | A: `Text` + `CF` · B: `Text` |
| [HASTE](../papers/haste.md) | arXiv’26 | IV × Training | `E-commerce` | A: `Text` · B: `MM` |
| [HCGRec](../papers/hcgrec.md) | CIKM’26 | IV × Training | `E-commerce` | `unknown` |
| [HoloRec](../papers/holorec.md) | arXiv’26 | III × Tokenization | `E-commerce` | `unknown` |
| [IBA](../papers/iba.md) | arXiv’26 | V × Backbone | `E-commerce` · `Short video / Live` | `Text` |
| [IDM/CMM](../papers/idm-cmm.md) | arXiv’26 | IV × Training | `E-commerce` | `Text` |
| [ISD](../papers/isd.md) | arXiv’26 | IV × Inference | `E-commerce` | `Text` |
| [JevRec](../papers/jevrec.md) | arXiv’26 | V × Tokenization | `E-commerce` | `Text` |
| [KL-MOPD](../papers/kl-mopd.md) | arXiv’26 | IV × Training | `E-commerce` · `Ads` | `CF` |
| [Latte](../papers/latte.md) | arXiv’26 | III × Backbone | `E-commerce` · `Music` | `unknown` |
| [LESSRec](../papers/lessrec.md) | arXiv’26 | III × Backbone | `E-commerce` | A: `Text` · B: `Text` + `CF` |
| [LION](../papers/lion.md) | CIKM’26 | VI × Backbone | `E-commerce` | `Text` |
| [LoopGR](../papers/loopgr.md) | arXiv’26 | V × Backbone | `E-commerce` · `unknown (industrial)` | `Text` |
| [MACRec](../papers/macrec.md) | AAAI’26 | I × Tokenization | `E-commerce` | text: `Text` · image: `Img` |
| [MDGR](../papers/mdgr.md) | arXiv’26 | III × Backbone | `E-commerce` | `Text` |
| [Merge-and-Branch](../papers/merge-and-branch.md) | arXiv’26 | V × Backbone | `E-commerce` | `Text` |
| [MMQ](../papers/mmq.md) | WSDM’26 | I × Tokenization | `E-commerce` · `Ads` | `Text` + `Img` |
| [MSCGRec](../papers/mscgrec.md) | arXiv’26 | I × Tokenization | `E-commerce` · `Short video / Live` | image: `Img` · text: `Text` · collaborative: `CF` |
| [MuSID-KD](../papers/musid-kd.md) | arXiv’26 | IV × Training | `E-commerce` · `Games` | `unknown` |
| [NAU](../papers/nau.md) | arXiv’26 | IV × Training | `E-commerce` | `unknown` |
| [NEZHA](../papers/nezha.md) | WWW’26 Industry | V × Inference | `E-commerce` · `POI / Local` · `Ads` · `Search` | `Text` |
| [OneChord](../papers/onechord.md) | arXiv’26 | IV × Training | `E-commerce` | `unknown` |
| [OneMall](../papers/onemall.md) | CIKM’26 | Paradigms, Systems and Benchmarks | `E-commerce` | A: `Text` + `Img` + `CF` · B: `Text` + `Img` + `CF` · C: `CF` + `unknown` |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V × Inference | `E-commerce` · `POI / Local` | `Text` + `CF` |
| [Pctx](../papers/pctx.md) | CIKM’26 | I × Tokenization | `E-commerce` | `Text` + `CF` |
| [PFA](../papers/pfa.md) | arXiv’26 | V × Inference | `E-commerce` · `Ads` | `unknown` |
| [PROMISE](../papers/promise.md) | arXiv’26 | III × Inference | `E-commerce` · `Short video / Live` | `Text` |
| [QuaSID](../papers/quasid.md) | KDD’26 ADS | II × Tokenization | `E-commerce` | `Text` + `Img` + `CF` |
| [R3-VAE](../papers/r3-vae.md) | arXiv’26 | II × Tokenization | `E-commerce` · `Music` · `Movie` · `News` | `Text` |
| [RAGR](../papers/ragr.md) | arXiv’26 | I × Training | `E-commerce` | item: `Text` · review: `Text` |
| [RecoChain](../papers/recochain.md) | arXiv’26 | IV × Backbone | `E-commerce` | `MM` |
| [REGER](../papers/reger.md) | arXiv’26 | I × Training | `E-commerce` | `Text` |
| [ReSID](../papers/resid.md) | arXiv’26 | I × Representation | `E-commerce` | `Attr` + `CF` |
| [Retrieval-Grounded-Credit](../papers/retrieval-grounded-credit.md) | arXiv’26 | IV × Training | `E-commerce` | `Text` |
| [RoFiGR](../papers/rofigr.md) | arXiv’26 | I × Tokenization | `E-commerce` | text: `Text` + `Img` + `CF` · image: `Text` + `Img` + `CF` |
| [S2GR](../papers/s2gr.md) | KDD’26 | III × Backbone | `E-commerce` · `Short video / Live` | `Text` + `CF` |
| [SAGE-SID](../papers/sage-sid.md) | arXiv’26 | IV × Training | `E-commerce` · `Short video / Live` · `Ads` | `Text` + `Img` |
| [SAHL](../papers/sahl.md) | arXiv’26 | IV × Training | `E-commerce` | `Text` |
| [SAPO](../papers/sapo.md) | arXiv’26 | IV × Training | `E-commerce` | `Text` |
| [SCRec](../papers/screc.md) | RecSys’26 | I × Representation | `E-commerce` | `Text` + `CF` |
| [SID-MLP](../papers/sid-mlp.md) | arXiv’26 | V × Backbone | `E-commerce` | `Text` |
| [SIDReasoner](../papers/sidreasoner.md) | KDD’26 | III × Training | `E-commerce` | `Text` |
| [SIDScope](../papers/sidscope.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `E-commerce` · `POI / Local` | `unknown` |
| [SLIDE](../papers/slide.md) | arXiv’26 | IV × Training | `E-commerce` · `Search` | `unknown` |
| [SpecGR](../papers/specgr.md) | AAAI’26 | VI × Inference | `E-commerce` | `Text` |
| [SPRINT](../papers/sprint.md) | arXiv’26 | V × Backbone | `E-commerce` · `POI / Local` | `Text` |
| [SST](../papers/sst.md) | CIKM’26 | III × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [STAMP](../papers/stamp.md) | arXiv’26 | V × Backbone | `E-commerce` | A: `Text` · B: `Text` + `Img` + `unknown` |
| [STATIC](../papers/static.md) | KDD’26 ADS | V × Inference | `E-commerce` · `Video` | `unknown` |
| [SynGR](../papers/syngr.md) | ICML’26 | I × Training | `E-commerce` | text: `Text` · image: `Img` |
| [TCBSA](../papers/tcbsa.md) | arXiv’26 | IV × Inference | `E-commerce` · `POI / Local` | `Text` |
| [Tlow](../papers/tlow.md) | CIKM’26 Applied | I × Tokenization | `E-commerce` · `Image / Article` | A: `Text` · B: `Text` + `Img` |
| [Token-Weighted](../papers/token-weighted.md) | CIKM’26 | IV × Training | `E-commerce` · `POI / Local` · `Movie` | `Text` |
| [TopoGR](../papers/topogr.md) | arXiv’26 | III × Tokenization | `E-commerce` | `Text` |
| [TRACER](../papers/tracer.md) | NeurIPS’26 | IV × Tokenization | `E-commerce` | `Text` |
| [TriAlignGR](../papers/trialigngr.md) | arXiv’26 | I × Representation | `E-commerce` | `Text` + `Img` |
| [TrieRec](../papers/trierec.md) | NeurIPS’26 | III × Backbone | `E-commerce` · `Movie` | `Text` |
| [UGR](../papers/ugr.md) | KDD’26 | IV × Training | `E-commerce` · `POI / Local` | `Text` |
| [UniRec](../papers/unirec.md) | arXiv’26 | I × Tokenization | `E-commerce` | `MM` + `Attr` |
| [UniSGR-V2](../papers/unisgr-v2.md) | arXiv’26 | I × Backbone | `E-commerce` | `unknown` |
| [UniSID](../papers/unisid.md) | arXiv’26 | I × Tokenization | `Ads` · `E-commerce` | `Text` + `Img` |
| [UniTok](../papers/unitok.md) | AAAI’26 | VI × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [V-STAR](../papers/v-star.md) | KDD’26 | IV × Training | `E-commerce` · `Ads` | `unknown` |
| [VarLenRec (TIGER)](../papers/varlenrec-tiger.md) | arXiv’26 | I × Tokenization | `E-commerce` · `POI / Local` | `Text` |

## POI / Local

> 44 papers. Point-of-interest, check-in, and local-life service recommendation (including Yelp, Gowalla, Foursquare, etc.).

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [CID](../papers/cid.md) | SIGIR-AP’23 | II × Tokenization | `E-commerce` · `POI / Local` | `CF` |
| [EAGER](../papers/eager.md) | KDD’24 | I × Backbone | `E-commerce` · `POI / Local` | semantic: `Text` · behavior: `CF` |
| [IDGenRec](../papers/idgenrec.md) | SIGIR’24 | III × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [LETTER](../papers/letter.md) | CIKM’24 | I × Tokenization | `E-commerce` · `POI / Local` | `Text` + `CF` |
| [SEATER](../papers/seater.md) | SIGIR-AP’24 | V × Tokenization | `POI / Local` · `E-commerce` · `News` · `Short video / Live` | `CF` |
| [SIIT](../papers/siit.md) | arXiv’24 | III × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [TransRec](../papers/transrec.md) | KDD’24 | II × Tokenization | `E-commerce` · `POI / Local` | id: – · title: `Text` · attribute: `Text` |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `POI / Local` | `Attr` + `Geo` + `Time` + `CF` |
| [GRAM](../papers/gram.md) | ACL’25 | I × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `POI / Local` | `Attr` + `Geo` + `CF` |
| [OneLoc](../papers/oneloc.md) | arXiv’25 | I × Representation | `POI / Local` | `MM` + `Geo` |
| [QT-Mob](../papers/qt-mob.md) | KDD’25 | I × Tokenization | `POI / Local` | `Text` + `Geo` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `News` · `Movie` · `Short video / Live` · `Book` · `POI / Local` · `Games` · `E-commerce` · `Travel / Hotel` | `Text` |
| [Spacetime-GR](../papers/spacetime-gr.md) | arXiv’25 | I × Backbone | `POI / Local` | `Geo` |
| [Align3GR](../papers/align3gr.md) | AAAI’26 | III × Tokenization | `E-commerce` · `POI / Local` · `Ads` | `Text` + `CF` |
| [APAO](../papers/apao.md) | KDD’26 | IV × Training | `E-commerce` · `POI / Local` | `Text` |
| [AWARE](../papers/aware.md) | arXiv’26 | VI × Training | `POI / Local` | `Text` + `Geo` |
| [CausalDPO](../papers/causaldpo.md) | ICML’26 | VI × Training | `POI / Local` · `Movie` · `Book` | `n/a` |
| [CITE](../papers/cite.md) | Electronics’26 | I × Inference | `E-commerce` · `POI / Local` | `Text` |
| [DIGER](../papers/diger.md) | SIGIR’26 | II × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [DOS](../papers/dos.md) | WWW’26 Short | III × Tokenization | `POI / Local` | `Text` + `CF` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | `POI / Local` · `Search` | `Text` + `Geo` + `CF` |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV × Training | `POI / Local` · `E-commerce` · `Ads` · `Search` | A: `Text` · B: `Text` + `CF` |
| [GR-Generalize](../papers/gr-generalize.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `E-commerce` · `Games` · `POI / Local` | `Text` |
| [GrIS (RecDMoN / RQ-GAE)](../papers/gris-recdmon-rq-gae.md) | CIKM’26 | I × Tokenization | `E-commerce` · `News` · `POI / Local` | `Text` + `CF` |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II × Tokenization | `POI / Local` | `Text` + `Img` + `Geo` + `CF` |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I × Representation | `POI / Local` | `Text` + `Attr` + `Geo` |
| [LGRID](../papers/lgrid.md) | arXiv’26 | I × Representation | `POI / Local` | `Text` + `Geo` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `POI / Local` | `Text` + `Geo` + `Attr` + `CF` |
| [NEZHA](../papers/nezha.md) | WWW’26 Industry | V × Inference | `E-commerce` · `POI / Local` · `Ads` · `Search` | `Text` |
| [OneLatent](../papers/onelatent.md) | arXiv’26 | V × Training | `Ads` · `POI / Local` | `MM` |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V × Inference | `E-commerce` · `POI / Local` | `Text` + `CF` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I × Tokenization | `POI / Local` · `Search` | `Text` + `Geo` |
| [ROS](../papers/ros.md) | ACL’26 | I × Tokenization | `POI / Local` | `Text` + `Geo` |
| [SIDScope](../papers/sidscope.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `E-commerce` · `POI / Local` | `unknown` |
| [SPAR](../papers/spar.md) | arXiv’26 | I × Representation | `POI / Local` | `Text` + `Geo` |
| [SPRINT](../papers/sprint.md) | arXiv’26 | V × Backbone | `E-commerce` · `POI / Local` | `Text` |
| [SST](../papers/sst.md) | CIKM’26 | III × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [TCBSA](../papers/tcbsa.md) | arXiv’26 | IV × Inference | `E-commerce` · `POI / Local` | `Text` |
| [Think2Go](../papers/think2go.md) | KDD’26 | III × Training | `POI / Local` | `unknown` |
| [Token-Weighted](../papers/token-weighted.md) | CIKM’26 | IV × Training | `E-commerce` · `POI / Local` · `Movie` | `Text` |
| [UGR](../papers/ugr.md) | KDD’26 | IV × Training | `E-commerce` · `POI / Local` | `Text` |
| [UniTok](../papers/unitok.md) | AAAI’26 | VI × Tokenization | `E-commerce` · `POI / Local` | `Text` |
| [VarLenRec (TIGER)](../papers/varlenrec-tiger.md) | arXiv’26 | I × Tokenization | `E-commerce` · `POI / Local` | `Text` |

## Short video / Live

> 21 papers. Short-video feed and live-streaming recommendation (including Kuaishou, KuaiRand, Douyin, etc.).

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [Molar](../papers/molar.md) | arXiv’24 | I × Representation | `E-commerce` · `Movie` · `Short video / Live` | `n/a` |
| [SEATER](../papers/seater.md) | SIGIR-AP’24 | V × Tokenization | `POI / Local` · `E-commerce` · `News` · `Short video / Live` | `CF` |
| [FlexCode](../papers/flexcode.md) | arXiv’25 | I × Tokenization | `E-commerce` · `Short video / Live` · `unknown (industrial)` | semantic: `Text` + `CF` · collaborative: `CF` |
| [HiD-VAE](../papers/hid-vae.md) | arXiv’25 | II × Tokenization | `E-commerce` · `Short video / Live` | `Text` + `Attr` |
| [OneRec](../papers/onerec.md) | arXiv’25 | Paradigms, Systems and Benchmarks | `Short video / Live` | `MM` + `CF` |
| [OneRec-Think](../papers/onerec-think.md) | arXiv’25 | III × Training | `E-commerce` · `Short video / Live` | `MM` + `CF` |
| [OneRec-V2](../papers/onerec-v2.md) | arXiv’25 | V × Backbone | `Short video / Live` | `Text` + `Img` + `CF` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `News` · `Movie` · `Short video / Live` · `Book` · `POI / Local` · `Games` · `E-commerce` · `Travel / Hotel` | `Text` |
| [DualGR](../papers/dualgr.md) | WWW’26 Short | VI × Backbone | `Short video / Live` | `unknown` |
| [Dynamic-Single-Codebook](../papers/dynamic-single-codebook.md) | arXiv’26 | V × Tokenization | `E-commerce` · `Short video / Live` · `unknown (industrial)` | `unknown` |
| [IBA](../papers/iba.md) | arXiv’26 | V × Backbone | `E-commerce` · `Short video / Live` | `Text` |
| [MMGRec](../papers/mmgrec.md) | TOMM’26 | I × Tokenization | `Movie` · `Short video / Live` | `Text` + `Img` + `Audio` + `CF` |
| [MSCGRec](../papers/mscgrec.md) | arXiv’26 | I × Tokenization | `E-commerce` · `Short video / Live` | image: `Img` · text: `Text` · collaborative: `CF` |
| [OneLive](../papers/onelive.md) | KDD’26 ADS | VI × Tokenization | `Short video / Live` | `Text` + `Img` + `Audio` + `CF` |
| [OneRec-V2-Quantized](../papers/onerec-v2-quantized.md) | arXiv’26 | V × Inference | `Short video / Live` | `Text` + `Img` + `CF` |
| [PLUM](../papers/plum.md) | WWW’26 | Paradigms, Systems and Benchmarks | `Long video` · `Short video / Live` | `MM` + `CF` |
| [PROMISE](../papers/promise.md) | arXiv’26 | III × Inference | `E-commerce` · `Short video / Live` | `Text` |
| [ReRankID](../papers/rerankid.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Short video / Live` | `Text` |
| [S2GR](../papers/s2gr.md) | KDD’26 | III × Backbone | `E-commerce` · `Short video / Live` | `Text` + `CF` |
| [SAGE-SID](../papers/sage-sid.md) | arXiv’26 | IV × Training | `E-commerce` · `Short video / Live` · `Ads` | `Text` + `Img` |
| [SnapLGR](../papers/snaplgr.md) | arXiv’26 | II × Tokenization | `Short video / Live` | `Text` + `Img` + `CF` |

## Ads

> 17 papers. Online advertising and sponsored recommendation.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [ADC-SID](../papers/adc-sid.md) | arXiv’25 | I × Tokenization | `E-commerce` · `Ads` | `Text` + `Img` + `CF` |
| [COBRA](../papers/cobra.md) | NeurIPS’25 | I × Backbone | `E-commerce` · `Ads` | `Text` |
| [DAS](../papers/das.md) | CIKM’25 | I × Tokenization | `Ads` | `Text` + `CF` |
| [Align3GR](../papers/align3gr.md) | AAAI’26 | III × Tokenization | `E-commerce` · `POI / Local` · `Ads` | `Text` + `CF` |
| [CMRec](../papers/cmrec.md) | CIKM’26 Short | VI × Training | `Ads` · `E-commerce` | `Text` + `Img` + `CF` |
| [GEM-Rec](../papers/gem-rec.md) | arXiv’26 | IV × Training | `Games` · `E-commerce` · `Ads` | `Text` |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV × Training | `POI / Local` · `E-commerce` · `Ads` · `Search` | A: `Text` · B: `Text` + `CF` |
| [GR4AD-X](../papers/gr4ad-x.md) | arXiv’26 | III × Tokenization | `Ads` | `unknown` |
| [GRC](../papers/grc.md) | CIKM’26 | III × Inference | `E-commerce` · `Ads` | `Text` |
| [KL-MOPD](../papers/kl-mopd.md) | arXiv’26 | IV × Training | `E-commerce` · `Ads` | `CF` |
| [MMQ](../papers/mmq.md) | WSDM’26 | I × Tokenization | `E-commerce` · `Ads` | `Text` + `Img` |
| [NEZHA](../papers/nezha.md) | WWW’26 Industry | V × Inference | `E-commerce` · `POI / Local` · `Ads` · `Search` | `Text` |
| [OneLatent](../papers/onelatent.md) | arXiv’26 | V × Training | `Ads` · `POI / Local` | `MM` |
| [PFA](../papers/pfa.md) | arXiv’26 | V × Inference | `E-commerce` · `Ads` | `unknown` |
| [SAGE-SID](../papers/sage-sid.md) | arXiv’26 | IV × Training | `E-commerce` · `Short video / Live` · `Ads` | `Text` + `Img` |
| [UniSID](../papers/unisid.md) | arXiv’26 | I × Tokenization | `Ads` · `E-commerce` | `Text` + `Img` |
| [V-STAR](../papers/v-star.md) | KDD’26 | IV × Training | `E-commerce` · `Ads` | `unknown` |

## Movie

> 12 papers. Movie recommendation (including MovieLens, Douban Movie, Netflix, etc.).

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [Molar](../papers/molar.md) | arXiv’24 | I × Representation | `E-commerce` · `Movie` · `Short video / Live` | `n/a` |
| [AtSpeed](../papers/atspeed.md) | ICLR’25 | V × Inference | `E-commerce` · `Movie` · `Book` | `Text` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `News` · `Movie` · `Short video / Live` · `Book` · `POI / Local` · `Games` · `E-commerce` · `Travel / Hotel` | `Text` |
| [TokenRec](../papers/tokenrec.md) | TKDE’25 | I × Tokenization | `Music` · `Movie` · `E-commerce` | `CF` |
| [CausalDPO](../papers/causaldpo.md) | ICML’26 | VI × Training | `POI / Local` · `Movie` · `Book` | `n/a` |
| [Deco](../papers/deco.md) | arXiv’26 | V × Backbone | `E-commerce` · `Movie` · `Music` | A: `Text` · B: `unknown` |
| [GenCDR](../papers/gencdr.md) | AAAI’26 | VI × Tokenization | `E-commerce` · `Book` · `Movie` | `Text` + `unknown` |
| [MMGRec](../papers/mmgrec.md) | TOMM’26 | I × Tokenization | `Movie` · `Short video / Live` | `Text` + `Img` + `Audio` + `CF` |
| [R3-VAE](../papers/r3-vae.md) | arXiv’26 | II × Tokenization | `E-commerce` · `Music` · `Movie` · `News` | `Text` |
| [SPRIG](../papers/sprig.md) | CIKM’26 Short | I × Tokenization | `Movie` · `Music` | A: `Text` · B: `Audio` |
| [Token-Weighted](../papers/token-weighted.md) | CIKM’26 | IV × Training | `E-commerce` · `POI / Local` · `Movie` | `Text` |
| [TrieRec](../papers/trierec.md) | NeurIPS’26 | III × Backbone | `E-commerce` · `Movie` | `Text` |

## Music

> 10 papers. Music track and artist recommendation (including Last.fm, Spotify, etc.).

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [PSRQ](../papers/psrq.md) | CIKM’25 | I × Tokenization | `E-commerce` · `Music` | text: `Text` · image: `Img` · audio: `Audio` · joint_Amazon: `Text` + `Img` · joint_Music: `Text` + `Audio` |
| [TokenRec](../papers/tokenrec.md) | TKDE’25 | I × Tokenization | `Music` · `Movie` · `E-commerce` | `CF` |
| [CAPE](../papers/cape.md) | arXiv’26 | I × Inference | `E-commerce` · `Music` | `Text` |
| [Deco](../papers/deco.md) | arXiv’26 | V × Backbone | `E-commerce` · `Movie` · `Music` | A: `Text` · B: `unknown` |
| [DPE-Rec](../papers/dpe-rec.md) | arXiv’26 | IV × Training | `Music` · `E-commerce` | A: `unknown` · B: `Text` + `Img` |
| [Gryphon](../papers/gryphon.md) | CIKM’26 Short | IV × Backbone | `Music` | `unknown` |
| [Latte](../papers/latte.md) | arXiv’26 | III × Backbone | `E-commerce` · `Music` | `unknown` |
| [NEO](../papers/neo.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Music` · `Podcast` · `Book` · `Search` | A: `Text` · B: `Audio` |
| [R3-VAE](../papers/r3-vae.md) | arXiv’26 | II × Tokenization | `E-commerce` · `Music` · `Movie` · `News` | `Text` |
| [SPRIG](../papers/sprig.md) | CIKM’26 Short | I × Tokenization | `Movie` · `Music` | A: `Text` · B: `Audio` |

## Search

> 10 papers. Product search, content search, and joint search–recommendation.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [LMIndexer](../papers/lmindexer.md) | ICML’24 | I × Tokenization | `E-commerce` · `Search` | `Text` |
| [FORGE](../papers/forge.md) | KDD’26 | Paradigms, Systems and Benchmarks | `E-commerce` · `Search` | `Text` + `Img` + `CF` |
| [GenSAR](../papers/gensar.md) | RecSys’25 | I × Tokenization | `E-commerce` · `Search` | semantic: `Text` + `CF` · collaborative: `Text` + `CF` |
| [PSI](../papers/psi.md) | arXiv’25 | II × Tokenization | `E-commerce` · `Search` | `Text` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | `POI / Local` · `Search` | `Text` + `Geo` + `CF` |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV × Training | `POI / Local` · `E-commerce` · `Ads` · `Search` | A: `Text` · B: `Text` + `CF` |
| [NEO](../papers/neo.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Music` · `Podcast` · `Book` · `Search` | A: `Text` · B: `Audio` |
| [NEZHA](../papers/nezha.md) | WWW’26 Industry | V × Inference | `E-commerce` · `POI / Local` · `Ads` · `Search` | `Text` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I × Tokenization | `POI / Local` · `Search` | `Text` + `Geo` |
| [SLIDE](../papers/slide.md) | arXiv’26 | IV × Training | `E-commerce` · `Search` | `unknown` |

## News

> 6 papers. News article recommendation (including MIND, etc.).

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [CoST](../papers/cost.md) | RecSys’24 | I × Tokenization | `News` · `E-commerce` | `Text` |
| [SEATER](../papers/seater.md) | SIGIR-AP’24 | V × Tokenization | `POI / Local` · `E-commerce` · `News` · `Short video / Live` | `CF` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `News` · `Movie` · `Short video / Live` · `Book` · `POI / Local` · `Games` · `E-commerce` · `Travel / Hotel` | `Text` |
| [GrIS (RecDMoN / RQ-GAE)](../papers/gris-recdmon-rq-gae.md) | CIKM’26 | I × Tokenization | `E-commerce` · `News` · `POI / Local` | `Text` + `CF` |
| [Intent-Driven-News](../papers/intent-driven-news.md) | ACL’26 Industry | III × Training | `News` | `Text` |
| [R3-VAE](../papers/r3-vae.md) | arXiv’26 | II × Tokenization | `E-commerce` · `Music` · `Movie` · `News` | `Text` |

## Book

> 5 papers. Book and audiobook recommendation (including Douban Book, Goodreads, etc.).

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [AtSpeed](../papers/atspeed.md) | ICLR’25 | V × Inference | `E-commerce` · `Movie` · `Book` | `Text` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `News` · `Movie` · `Short video / Live` · `Book` · `POI / Local` · `Games` · `E-commerce` · `Travel / Hotel` | `Text` |
| [CausalDPO](../papers/causaldpo.md) | ICML’26 | VI × Training | `POI / Local` · `Movie` · `Book` | `n/a` |
| [GenCDR](../papers/gencdr.md) | AAAI’26 | VI × Tokenization | `E-commerce` · `Book` · `Movie` | `Text` + `unknown` |
| [NEO](../papers/neo.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Music` · `Podcast` · `Book` · `Search` | A: `Text` · B: `Audio` |

## Games

> 5 papers. Video game platform recommendation (including Steam).

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [LIGER](../papers/liger.md) | arXiv’24 | VI × Inference | `E-commerce` · `Games` | `Text` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `News` · `Movie` · `Short video / Live` · `Book` · `POI / Local` · `Games` · `E-commerce` · `Travel / Hotel` | `Text` |
| [GEM-Rec](../papers/gem-rec.md) | arXiv’26 | IV × Training | `Games` · `E-commerce` · `Ads` | `Text` |
| [GR-Generalize](../papers/gr-generalize.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `E-commerce` · `Games` · `POI / Local` | `Text` |
| [MuSID-KD](../papers/musid-kd.md) | arXiv’26 | IV × Training | `E-commerce` · `Games` | `unknown` |

## Long video

> 3 papers. Long-form video platform recommendation.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [Netflix-SID-Comparison](../papers/netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | Paradigms, Systems and Benchmarks | `Long video` | `unknown` |
| [PLUM](../papers/plum.md) | WWW’26 | Paradigms, Systems and Benchmarks | `Long video` · `Short video / Live` | `MM` + `CF` |
| [SPAR-Youku](../papers/spar-youku.md) | arXiv’26 | I × Backbone | `Long video` | `unknown` |

## Image / Article

> 3 papers. Image discovery and article content recommendation.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [PinGER](../papers/pinger.md) | arXiv’26 | V × Backbone | `Image / Article` | `Text` + `Img` + `CF` |
| [PrefixMem](../papers/prefixmem.md) | arXiv’26 | III × Backbone | `Image / Article` | `MM` |
| [Tlow](../papers/tlow.md) | CIKM’26 Applied | I × Tokenization | `E-commerce` · `Image / Article` | A: `Text` · B: `Text` + `Img` |

## Podcast

> 1 paper. Podcast show and episode recommendation.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [NEO](../papers/neo.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Music` · `Podcast` · `Book` · `Search` | A: `Text` · B: `Audio` |

## Video

> 1 paper. General video platform recommendation.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [STATIC](../papers/static.md) | KDD’26 ADS | V × Inference | `E-commerce` · `Video` | `unknown` |

## Apps

> 1 paper. Mobile application recommendation.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [PCR-CA](../papers/pcr-ca.md) | KDD’26 | I × Tokenization | `Apps` | `Text` + `CF` |

## Food / Recipe

> 1 paper. Food and recipe recommendation.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [ColaRec](../papers/colarec.md) | CIKM’24 | I × Backbone | `E-commerce` · `Food / Recipe` | `CF` |

## Travel / Hotel

> 1 paper. Travel and hotel accommodation recommendation.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `News` · `Movie` · `Short video / Live` · `Book` · `POI / Local` · `Games` · `E-commerce` · `Travel / Hotel` | `Text` |

## Recruitment

> 1 paper. Job and recruitment recommendation.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [GTI](../papers/gti.md) | arXiv’26 | III × Training | `Recruitment` · `E-commerce` | A: `Text` + `CF` · B: `Text` |

## unknown (industrial)

> 6 papers. Industrial logs where the specific business vertical is not disclosed in the paper.

| Paper | Venue | Problem × Stage | Domain | SID Inputs |
| :--- | :--- | :--- | :--- | :--- |
| [FlexCode](../papers/flexcode.md) | arXiv’25 | I × Tokenization | `E-commerce` · `Short video / Live` · `unknown (industrial)` | semantic: `Text` + `CF` · collaborative: `CF` |
| [CapsID](../papers/capsid.md) | arXiv’26 | I × Tokenization | `E-commerce` · `unknown (industrial)` | A: `unknown` · B: `Text` + `Img` + `CF` |
| [DASO](../papers/daso.md) | arXiv’26 | IV × Training | `E-commerce` · `unknown (industrial)` | `Text` + `unknown` |
| [Dynamic-Single-Codebook](../papers/dynamic-single-codebook.md) | arXiv’26 | V × Tokenization | `E-commerce` · `Short video / Live` · `unknown (industrial)` | `unknown` |
| [LoopGR](../papers/loopgr.md) | arXiv’26 | V × Backbone | `E-commerce` · `unknown (industrial)` | `Text` |
| [MBGR](../papers/mbgr.md) | arXiv’26 | VI × Tokenization | `unknown (industrial)` | `unknown` |
