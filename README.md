# sqlite-lease-fencing-lab

## Français

Reproduire un ancien détenteur de bail avec jetons de clôture.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m sqlite_lease_fencing_lab examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Rejoue un détenteur expiré A après acquisition B avec vrais UPDATE SQLite ; le jeton est vérifié par la ressource, pas seulement par le détenteur du bail.

### Limites

Ordonnancement déterministe local sans serveur de bail ni expiration réelle ; accepte les reprises au même jeton sans garantir l’idempotence du contenu.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Reproduce a stale lease holder with fencing tokens.

Synthetic data; no network access or secret required.

```sh
python -m sqlite_lease_fencing_lab examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Replays expired holder A after B acquisition with actual SQLite UPDATEs; token enforcement lives at the resource, not only at the lease holder.

### Limits

Deterministic local schedule without lease server or actual expiry; same-token retries allowed without content idempotence guarantee.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Reproducir un titular de arrendamiento obsoleto con tokens de exclusión.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m sqlite_lease_fencing_lab examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Reproduce titular A expirado tras adquisición B con UPDATE SQLite reales; recurso valida token, no solo titular del arrendamiento.

### Límites

Secuencia local determinista sin servidor de arrendamiento ni expiración real; reintentos con mismo token sin garantía de idempotencia del contenido.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
