# Phishing Detection Project

## Team Contributions

| Team Member   | Contributions                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Talha Taiyoub** | Contributed to every aspect of the project, including data preprocessing, model development, data augmentation, training, testing, and evaluation. |

## Data Augmentation

To improve the robustness of the phishing detection model, several data augmentation techniques were employed to generate diverse URL variations. These techniques include:

1. **Synonym Replacement (SR)**: Replacing words in the URL with their synonyms to create variations without altering the meaning.
2. **Random Insertion (RI)**: Adding security-related terms or random characters to the URL to simulate common phishing attempts.
3. **Random Deletion (RD)**: Removing characters or words from the URL, which can often be used in obfuscating phishing sites.
4. **Random Swap (RS)**: Swapping parts of the URL, such as changing the order of subdomains or paths.
5. **Homoglyph Substitution**: Replacing characters in the URL with visually similar lookalikes (e.g., "g00gle.com" instead of "google.com").
6. **Synthetic URL Generation**: Creating completely new, synthetic phishing-like URLs based on known patterns of phishing sites.
7. **TLD Manipulation**: Altering domain extensions (e.g., changing ".com" to ".xyz") to simulate deceptive domain names.

These methods help to create a more diverse and comprehensive dataset for training the model.

## Performance Metrics (5-Fold Cross-Validation)

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 0.9753 |
| Precision | 0.9680 |
| Recall    | 0.9654 |
| F1-Score  | 0.9666 |


## Project Completion Plan

The final phase of this project involves the following steps:

- **API Development**: I'll create an API that leverages the trained model for phishing detection. This will allow users to input URLs and receive predictions regarding their legitimacy.
- **Browser Extension**: A browser extension will be built using this API, enabling users to easily check whether a website is phishing or legitimate while browsing.

These final steps will make the phishing detection model accessible and usable for a wide audience, improving web security for everyday users.
