# TOPSIS: Technique for Order Preference by Similarity to Ideal Solution

## 📖 Overview
TOPSIS is a **multi-criteria decision-making (MCDM)** method that helps rank alternatives when multiple, often conflicting criteria are involved.  
The core idea is simple: the best option should be **closest to the ideal solution** and **farthest from the worst solution**.

---

## ⚙️ How TOPSIS Works

1. **Construct the Decision Matrix**  
   - List all alternatives (options to choose from).  
   - Define evaluation criteria (e.g., cost, performance, reliability).  

2. **Normalize the Matrix**  
   - Convert values into comparable scales using normalization.  
   - Ensures criteria with different units (like dollars vs. hours) can be compared fairly.  

3. **Apply Weights**  
   - Assign importance to each criterion (e.g., performance = 0.5, cost = 0.3, reliability = 0.2).  
   - Multiply normalized values by their respective weights.  

4. **Determine Ideal & Negative-Ideal Solutions**  
   - **Positive Ideal Solution (PIS):** Best values across all criteria.  
   - **Negative Ideal Solution (NIS):** Worst values across all criteria.
  
5. **Calculate Distances**  
   - Compute Euclidean distance of each alternative from PIS and NIS.  

6. **Compute Relative Closeness**  
   - Closeness = Distance to NIS / (Distance to PIS + Distance to NIS).  
   - Higher closeness → better ranking.  

7. **Rank Alternatives**  
   - Sort options based on closeness values.  
   - The top-ranked option is the most preferred.  

---

## 📊 Example
Imagine choosing a laptop based on **Price, Performance, and Battery Life**:
- TOPSIS normalizes these values, applies weights, and calculates which laptop is closest to the "ideal" (low price, high performance, long battery life).  
- The final ranking shows which laptop offers the best balance across all criteria.
- !pip install Topsis-Anshul-102303930
- import topsis_anshul
- 

---

## 🔗 Project Links
- **PyPI Package:** [https://pypi.org/project/topsis-anshul-102303930/]  
- **Backend Link:** [https://github.com/AnshulKaushal27/topsis-backend]  
- **Frontend Link:** [https://github.com/AnshulKaushal27/topsis-frontend]  
- **Website Link:** [https://playful-sable-d77221.netlify.app/]  
