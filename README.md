# Besu Auto 🚀

Automated deployment tool for Hyperledger Besu blockchain networks with Docker support

## Features

- ✨ **One-command deployment** - Set up a complete Besu network instantly
- 🔐 **Multiple consensus algorithms** - IBFT2 and QBFT support
- 📊 **Flexible configuration** - Enterprise, Performance, and Performance_RPC profiles
- 🐳 **Docker-based** - Containerized nodes for easy management
- 🔧 **4 validator nodes + 1 RPC node** - Production-ready network setup
- ⚡ **Configurable block time** - TPS testing (0.5s) to stable (5s) options
- 🔄 **Soft reset mode** - Change profiles without regenerating keys
- 🧹 **Clean reset** - Easy cleanup and fresh start capability

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Hyperledger Besu CLI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nara020/besu-auto.git
cd besu-auto
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 🚀 Deploy Besu Network

Run the setup script to deploy your Besu network:

```bash
python setup_besu.py
```

During setup, you'll be prompted to choose:

**Mode Selection:**
- `1` - Full setup (generate new keys)
- `2` - Soft reset (keep keys, change profiles only)

**For Full Setup:**
1. **Consensus Algorithm**: IBFT2 or QBFT
2. **Block Generation Speed**:
   - TPS testing (0.5s) - Very fast for performance testing
   - Normal (2s) - Default, balanced
   - Stability-focused (5s) - Slower but stable
   - Custom - Enter your own value
3. **Validator Node Profile**: Enterprise or Performance
4. **RPC Node Profile**: Enterprise, Performance_RPC, or Performance

The script will automatically:
1. Generate validator keys using Besu CLI
2. Create genesis file with selected consensus
3. Configure 4 validator nodes + 1 RPC node
4. Set up Docker containers with fixed IPs
5. Generate validators.json and .env files

### 🧹 Clean and Reset

To remove all generated files and reset your environment:

```bash
python clean.py
```

This will:
- Remove config directory and genesis files
- Delete all node data directories
- Clean up docker-compose.yml and .env files
- Remove all *config.json files

## Network Configuration

After deployment, your network will have:

### Validator Nodes
| Node | HTTP Port | WS Port | P2P Port | Docker IP | Role |
|------|-----------|---------|----------|-----------|------|
| Node 1 | 8545 | - | 30303 | 192.168.100.11 | Validator/Bootnode |
| Node 2 | 8546 | - | 30304 | 192.168.100.12 | Validator |
| Node 3 | 8547 | - | 30305 | 192.168.100.13 | Validator |
| Node 4 | 8548 | - | 30306 | 192.168.100.14 | Validator |

### RPC Node
| Node | HTTP Port | WS Port | P2P Port | Docker IP | Role |
|------|-----------|---------|----------|-----------|------|
| Node 5 | 8550 | 8551 | 30307 | 192.168.100.15 | RPC Only |

### Network Settings
- **Chain ID**: 20250707
- **Initial Balance**: 1,000,000 ETH per validator
- **Gas Price**: 0 (free gas)
- **Network**: 192.168.100.0/24

## Project Structure

```
besu-auto/
├── setup_besu.py      # Main deployment script
├── clean.py           # Cleanup utility
├── requirements.txt   # Python dependencies
├── LICENSE           # MIT License
├── README.md         # This file
└── (Generated files after setup)
    ├── config/
    │   ├── genesis-{consensus}.json
    │   └── keys/      # Validator keys
    ├── node1-4/       # Validator node data
    ├── node5/         # RPC node data
    ├── docker-compose.yml
    ├── validators.json
    └── .env          # Node keys and addresses
```

## Example Workflow

```bash
# 1. Clean previous setup (if any)
python clean.py

# 2. Deploy a new network
python setup_besu.py
# Select: 1 (Full setup)
# Select: QBFT consensus
# Select: TPS testing (0.5s) for block speed
# Select: Performance profile for validators
# Select: Performance_RPC profile for RPC node

# 3. Start the network
docker-compose up -d

# 4. Check network status
docker ps

# 5. Test RPC endpoint
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' http://localhost:8545

# 6. Check validators (QBFT)
curl -X POST --data '{"jsonrpc":"2.0","method":"qbft_getValidatorsByBlockNumber","params":["latest"],"id":1}' http://localhost:8545

# 7. Soft reset (change profiles only)
python setup_besu.py
# Select: 2 (Soft reset)
# Select new profiles
docker-compose down && docker-compose up -d

# 8. Full reset and start fresh
python clean.py
python setup_besu.py
```

## Profiles

### Validator Profiles
- **Enterprise**: Balanced for stability and features
- **Performance**: Optimized for high throughput

### RPC Node Profiles
- **Enterprise**: Standard configuration
- **Performance_RPC**: Optimized for RPC workloads
- **Performance**: Maximum performance

## Performance Tuning

### Block Generation Speed Impact
- **0.5s**: ~2 TPS theoretical maximum (testing only)
- **2s**: ~0.5 TPS theoretical maximum (default)
- **5s**: ~0.2 TPS theoretical maximum (stable)

⚠️ Note: Actual TPS depends on transaction complexity and network conditions.

## Troubleshooting

### Besu CLI not found
```bash
# Install Besu
wget https://github.com/hyperledger/besu/releases/latest/download/besu-<version>.tar.gz
tar -xzf besu-*.tar.gz
sudo mv besu-*/bin/besu /usr/local/bin/
```

### Port conflicts
```bash
# Check ports
netstat -tulpn | grep -E '854[5-8]|8550|8551|303'
```

### Docker network issues
```bash
docker network rm besu-network
docker-compose up -d
```

## Contributing

Feel free to open issues or submit pull requests!

## License

MIT License - See [LICENSE](LICENSE) file for details

## Author

Created with ❤️ by nara020 for easy Besu blockchain deployment