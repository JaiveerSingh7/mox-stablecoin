# 🪙 Stablecoin Protocol (Vyper + Moccasin)

A minimal decentralized stablecoin protocol built using Vyper and Moccasin for smart contract development and testing.

## 📖 Overview

This project implements a collateralized debt position (CDP) system where users can deposit ETH to mint a dollar-pegged stablecoin, with automated liquidation mechanisms to maintain solvency.

---

## ⚙️ Features

### 🏦 1. Collateralized Minting
- Users can **deposit $200 worth of ETH**.
- They are allowed to **mint up to $50 of stablecoin**.
  - This results in a **4:1 collateral-to-debt ratio**.
- The protocol enforces a **minimum collateral ratio of 2:1**.

---

### 🛡 2. Collateral Ratio Enforcement
- If the **ETH price drops**, the protocol continuously checks the **collateral ratio**.
- Positions falling **below the 2:1 threshold** become eligible for liquidation.

---

### 🔨 3. Liquidation Mechanism
- Anyone can **liquidate undercollateralized positions**.
- Liquidators are incentivized to act quickly when ETH prices fall, ensuring system stability.

---

## 🧪 Stack

- **Vyper**: Smart contract language used for security and auditability.
- **Moccasin**: Test runner and development framework for Vyper.
- **ETH Price Feed**: Mock or oracle-integrated for testing ETH price volatility.
- **ERC20**: Stablecoin is implemented as a compliant ERC20 token.

---