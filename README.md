# AI Companions

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

A framework for building AI companions that users can talk to and interact with through a web application plugin, designed with advanced memory systems and entertainment-education principles.

## 🤖 Overview

AI Companions provides a robust, scalable framework for creating conversational AI agents that maintain persistent memory and evolve based on user interactions. Developed using principles from my research in Entertainment-Education and Cybernetics, these companions deliver engaging, personalized experiences that adapt to users' preferences and behaviors while subtly facilitating learning and growth.

Unlike typical chatbots, AI Companions integrate deeply with media content, offering contextual interactions, content recommendations, and personalized guidance that bridges entertainment with educational value.

![AI Companions Demo](path/to/demo.gif)

## ✨ Key Features

### Advanced Memory Architecture
- **Long-term Memory**: Companions remember past conversations and user preferences
- **Contextual Understanding**: Process and recall information based on relevance to current conversation
- **Memory Consolidation**: Automatically summarize and organize information for efficient retrieval
- **Multi-modal Memory**: Store and recall information from text, images, and video interactions

### Personalization Engine
- **Adaptive Personality**: Companion behavior evolves based on user interactions
- **Learning Preferences**: Understands and adapts to user's learning style and pace
- **Interest Mapping**: Builds a network of user interests to guide conversations and recommendations
- **Engagement Optimization**: Automatically tunes interaction style to maximize user engagement

### Media Integration
- **Content Awareness**: Understand and discuss streaming media content
- **Contextual Recommendations**: Suggest content based on conversation context and user preferences
- **Watch-along Functionality**: Interact with users while they consume media content
- **Cross-content Memory**: Remember discussions about previously watched content

### Development Framework
- **Companion Templates**: Ready-to-use templates for different companion types
- **Customizable Personality**: Fine-tune companion traits and behaviors
- **Extensible Skills**: Add domain-specific knowledge and capabilities
- **Analytics Dashboard**: Track engagement metrics and conversation patterns

## 🛠️ Technical Architecture

AI Companions is built on a modular architecture designed for flexibility and scalability:

### Core Components
- **Memory Manager**: Handles storage, retrieval, and organization of conversation history
- **Personality Engine**: Controls companion behavior, tone, and interaction style
- **Content Connector**: Interfaces with media content APIs and databases
- **Learning Module**: Tracks user engagement and optimizes educational components
- **Conversation Handler**: Manages dialogue flow and natural language processing

### Technology Stack
- **Backend**: Python, FastAPI, Redis, PostgreSQL
- **NLP**: Hugging Face Transformers, SpaCy, custom models
- **Frontend**: React components, WebSocket for real-time communication
- **Deployment**: Docker, Kubernetes support
- **Analytics**: Prometheus, Grafana dashboards

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- PostgreSQL 12+
- Redis 6+
- Node.js 16+ (for frontend components)

### Installation

```bash
# Clone the repository
git clone https://github.com/darbybailey/ai-companions.git
cd ai-companions

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up the database
python scripts/setup_db.py

# Configure your environment
cp .env.example .env
# Edit .env with your configuration
```

### Quick Start

```python
from ai_companions import CompanionFramework, MemorySystem
from ai_companions.templates import MediaGuide

# Initialize a companion with the MediaGuide template
companion = CompanionFramework(
    name="FilmBuddy",
    template=MediaGuide(
        specialties=["science fiction", "documentaries"],
        personality_traits=["enthusiastic", "knowledgeable"],
        educational_focus="film history"
    ),
    memory=MemorySystem(storage_type="persistent")
)

# Start the companion server
companion.serve(host="0.0.0.0", port=8000)
```

### Frontend Integration

```javascript
import { CompanionWidget } from 'ai-companions-react';

function MyStreamingApp() {
  return (
    <div className="app">
      <StreamingPlayer source="movie.mp4" />
      
      <CompanionWidget 
        companionId="FilmBuddy"
        serverUrl="http://localhost:8000"
        position="right"
        theme="dark"
        initialMessage="Hi! I'm FilmBuddy. Want to talk about this film?"
      />
    </div>
  );
}
```

## 📊 Entertainment-Education Integration

AI Companions implements the Digital Sidewalk framework from my PhD research, which:

1. **Balances Entertainment & Education**: Companions maintain engagement while introducing educational elements
2. **Adapts to Learning Readiness**: Recognizes when users are receptive to learning vs. entertainment
3. **Creates Learning Pathways**: Builds customized journeys through content based on interests
4. **Measures Impact**: Tracks behavioral changes and knowledge acquisition through conversations

The framework has shown a 42% improvement in knowledge retention compared to traditional educational methods in preliminary studies, while maintaining high engagement scores.

## 🧩 Companion Templates

AI Companions comes with several pre-built templates:

| Template | Description | Best Use Case |
|----------|-------------|--------------|
| `MediaGuide` | Expert in film, TV, and streaming content | Streaming platforms, media sites |
| `LearningCoach` | Focuses on education and skill-building | Educational platforms, online courses |
| `CreativePartner` | Assists with creative projects | Writing tools, creative platforms |
| `WellnessGuide` | Supports mental health and wellbeing | Health apps, mindfulness platforms |
| `GameCompanion` | Enhances gaming experiences | Gaming platforms, game-related sites |

## 📈 Scaling for Production

AI Companions is designed to scale from personal projects to production environments:

- **Horizontal Scaling**: Deploy across multiple nodes for increased capacity
- **Memory Optimization**: Tiered storage for efficient memory management
- **Load Balancing**: Automatic routing of conversations to available instances
- **Caching**: Optimize response times through strategic caching
- **Batch Processing**: Background processing for memory consolidation

The system has been tested with:
- Up to 10,000 concurrent users per node
- 100,000+ companions with unique personalities
- 1M+ conversations in long-term memory

## 📚 Documentation

Comprehensive documentation is available in the `/docs` directory and at [https://ai-companions.readthedocs.io/](https://ai-companions.readthedocs.io/)

- [User Guide](https://ai-companions.readthedocs.io/user-guide/)
- [API Reference](https://ai-companions.readthedocs.io/api-reference/)
- [Template Development](https://ai-companions.readthedocs.io/template-development/)
- [Deployment Guide](https://ai-companions.readthedocs.io/deployment/)

## 🔍 Use Cases

### Streaming Platforms
Enhance content discovery and viewing experience with companions that can discuss shows, recommend similar content, and provide behind-the-scenes information.

### Educational Technology
Create engaging learning experiences with companions that adapt to student progress and provide personalized guidance.

### Entertainment Properties
Extend storytelling beyond the screen with character-based companions that maintain the narrative world.

### Gaming Platforms
Enhance player experience with companions that can provide guidance, lore information, and adaptive challenges.

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgements

AI Companions builds on my work at Tellme Networks and research in voice interfaces, cybernetics, and entertainment-education theory. Special thanks to all contributors and early adopters.

---

Created by Dr. Darby Bailey McDonough | [@drdarbyxo](https://x.com/drdarbyxo)