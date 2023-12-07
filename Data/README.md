
## Synthèse du dataset

- **step**: Un indicateur de temps ou d'étape pour la transaction.
- **type**: Le type de transaction (PAYMENT, TRANSFER, CASH_OUT, DEBIT).
- **amount**: Le montant de la transaction.
- **nameOrig**: Le nom du client ou de l'entité d'origine.
- **oldbalanceOrg**: Le solde initial de l'entité d'origine avant la transaction.
- **newbalanceOrig**: Le nouveau solde de l'entité d'origine après la transaction.
- **nameDest**: Le nom du destinataire de la transaction.
- **oldbalanceDest**: Le solde initial du destinataire avant la transaction.
- **newbalanceDest**: Le nouveau solde du destinataire après la transaction.
- **isFraud**: Un indicateur binaire indiquant si la transaction est frauduleuse (1 pour vrai, 0 pour faux).
- **isFlaggedFraud**: Un indicateur binaire signalant si la transaction a été signalée comme frauduleuse.