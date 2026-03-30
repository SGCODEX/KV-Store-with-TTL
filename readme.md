# Unravel Assignment - Shivam Gupta

## KV Store with TTL

Problem Statement: Build an in-memory key-value store exposed via REST API. Support SET (with optional TTL in seconds), GET, and DELETE. Expired keys should behave as if they don't exist.

## Introduction

A simple in-memory key-value store built using Python and FastAPI.
This project mimics basic behavior of systems like Redis, supporting key storage with optional expiration (TTL).

## Features

* Set key-value pairs
* Optional TTL (Time-To-Live) in seconds
* Get values (auto-handles expired keys)
* Delete keys
* REST API using FastAPI
* Lazy expiration (keys are removed when accessed after expiry)

## How It Works

* Data is stored in a Python dictionary (in-memory).
* Each key stores:

  * `value`
  * `expiry` (timestamp in seconds)
* TTL is handled using Python’s `time.time()`.

### Expiry Logic (Lazy Deletion)

* Keys are **not actively cleaned in background**
* When a key is accessed using GET:

  * If expired → it is deleted immediately
  * If valid → value is returned

## Project Structure

```
kv-store/
│── main.py        # FastAPI server (API endpoints)
│── store.py       # Core key-value logic with TTL
│── models.py      # Request models (Pydantic)
```

## Installation

```bash
pip install fastapi uvicorn
```

## Running the Server

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### SET (Create / Update)

```
POST /set
```

Request Body:

```json
{
  "key": "otp",
  "value": "1234",
  "ttl": 5
}
```

* TTL is optional (in seconds)
* If key exists → it is overwritten

### GET

```
GET /get/{key}
```

Response:

```json
{
  "key": "otp",
  "value": "1234"
}
```

If expired or not found:

```json
{
  "message": "Key not found or expired"
}
```

### DELETE

```
DELETE /delete/{key}
```

## ⏳ TTL Behavior

* TTL is specified in **seconds**
* Internally converted to:

  ```
  expiry = current_time + ttl
  ```
* Expired keys behave as if they don’t exist

## Limitations

* Data is stored in memory → lost on server restart
* No background cleanup of expired keys
* Not thread-safe (single-thread usage recommended)

## Summary

This project demonstrates how to build a lightweight caching system with TTL using in-memory storage and REST APIs.