## API Endpoints

### 1. Get All Actors
**URL**: `/api/actors`  
**Method**: `GET`  
**Description**: Retrieves the entire list of actors.  

**Response**:
```json
[
    {
        "name": "John Doe",
        "gender": "male",
        "birth_date": "15 March 1990"
    },
    {
        "name": "Jane Doe",
        "gender": "female",
        "birth_date": "22 July 1985"
    }
]
```

---

### 2. Get Random Actors
**URL**: `/api/actors/random/<int:num>`  
**Method**: `GET`  
**Description**: Retrieves a random selection of actors.

**Parameters**:
- `num` (integer): Number of random actors to retrieve.

**Response**:
```json
[
    {
        "name": "John Doe",
        "gender": "male",
        "birth_date": "15 March 1990"
    }
]
```

---

### 3. Get Actor by Name
**URL**: `/api/actors/<string:name>`  
**Method**: `GET`  
**Description**: Retrieves an actor by their exact or fuzzy name match.

**Response**:
```json
{
    "name": "John Doe",
    "gender": "male",
    "birth_date": "15 March 1990"
}
```

---

### 4. Search Actors
**URL**: `/api/actors/search`  
**Method**: `GET`  
**Description**: Searches actors by query parameters.

**Query Parameters**:
- `name` (string, optional): Search by actor name (fuzzy matching not supported here).
- `gender` (string, optional): Filter by gender (case insensitive).
- `birth_date` (string, optional): Search by exact birth date (format: `DD Month YYYY`).
- `month` (string, optional): Filter actors born in a specific month (e.g., `March`).

**Example Request**:
```bash
curl "http://localhost:5000/api/actors/search?month=March"
```

**Response**:
```json
[
    {
        "name": "John Doe",
        "gender": "male",
        "birth_date": "15 March 1990"
    }
]
```

**Error Handling**:
- If no actors are found:
```json
{
    "message": "No actors found matching the criteria"
}
```
