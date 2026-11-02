## At a Glance

Key Findings: On the industrial dataset, ProGEO reports Hit@50 of 0.4243 against 0.4056 for RQ-Kmeans, and an average geographic clustering distance of 25.41 km against 46.71 km for RQ-OPQ (Table 1).

### 1. Why This Paper Matters

Local service platforms need recommendations that are relevant and also geographically reachable (Abstract). Semantic codebooks cluster items by content alone.

> "existing semantic codebooks neglect geographic constraints, often resulting in recommendations that are semantically relevant yet geographically unreachable." (Abstract)

ProGEO keeps standard semantic codewords and adds a geo-codeword that encodes each POI's position relative to its semantic cluster, so geography becomes part of the Semantic ID (SID) instead of a weak auxiliary feature (Abstract, Sec. 1).

Based on arXiv v1.

### 2. How It Works

*Figure source: Fig. 2, original paper.*

```mermaid
flowchart LR
    A[POI features] --> B[Two semantic layers]
    B --> C[Geo-centroid coordinates]
    C --> D[Geo-RoPE layer]
    D --> E[SID]
    E --> F[Fine-tuned LLM]
    F --> G[Nearby POIs]
```

#### Semantic Layers

The first two codebook layers cluster mixed feature vectors with cosine similarity as the metric and pass projection residuals to the next layer (Sec. 3.1). The SID has two standard codebook layers and one geo-codebook layer (Fig. 2).

#### Geo-Centroid Local Coordinates

POIs that share the same two-layer SID form a subset. The actual latitudes and longitudes of these POIs define a geographic centroid, and each POI's global position becomes polar coordinates around it (Sec. 1, Sec. 3.2).

#### Geo-RoPE

Geo-RoPE encodes each POI's offset from the centroid as complex-valued rotations of the residual from the second layer (Sec. 1, Sec. 3.3). The similarity between two rotated vectors then depends on both their semantic factors and their spatial relation.

> "We extend RoPE to the spatial domain, formalizing geographic proximity as rotary operations in high-dimensional feature space." (Sec. 3.3)

#### Generation

In the industrial setting, the LLM prompt contains the search query, the city, and a GeoHash of the user's location (Table 4).

### 3. Experimental Findings

- Geo-RoPE layer: applying Geo-RoPE only at the third clustering layer gives the highest CUR (7.67%) and ICR (57.08%) among the tested placements (Sec. 4.3.2, Fig. 5).
- Case study: with Geo-RoPE, the recommended POIs lie close to the user, while the variant without it returns a POI in another city (Sec. 4.5.2).

  > "when Geo-RoPE is introduced, the recommended POIs are concentrated much closer to the user, typically within a 6-kilometer radius." (Sec. 4.5.2)

### 4. Limitations & Critical Analysis

**Our analysis.**

- The geographic signal enters only the third SID token. This suggests that the generator still chooses the semantic cluster before it uses any spatial information.
- OneLoc uses plain `R-KM` codes; ProGEO adds a geo-codebook layer to the same kind of tokenizer (`R-KM+Geo-CB`).
- GNPR-SID also encodes geography in POI SIDs (`Attr+Geo+CF`) but uses a plain `RQ-VAE`, without a dedicated geo-codebook layer.
