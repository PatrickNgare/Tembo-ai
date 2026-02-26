import { useState, useRef, useEffect } from 'react'

const API_URL = 'http://localhost:8000'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [sessionId] = useState(() => `session_${Date.now()}`)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const sendMessage = async (e) => {
    e.preventDefault()
    if (!input.trim() || isLoading) return

    const userMessage = input.trim()
    setInput('')
    
    // Add user message
    setMessages(prev => [...prev, { role: 'user', content: userMessage }])
    setIsLoading(true)

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userMessage,
          session_id: sessionId
        })
      })

      if (!response.ok) throw new Error('Failed to get response')

      const data = await response.json()
      
      // Add assistant message with typing effect
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: data.answer,
        sources: data.sources,
        isTyping: true 
      }])

      // Remove typing flag after animation
      setTimeout(() => {
        setMessages(prev => prev.map((msg, i) => 
          i === prev.length - 1 ? { ...msg, isTyping: false } : msg
        ))
      }, 50)

    } catch (error) {
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: 'Samahani! (Sorry) I encountered an error. Please try again.',
        isError: true 
      }])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex flex-col">
      {/* Header */}
      <header className="bg-slate-800/50 backdrop-blur-sm border-b border-slate-700 px-4 py-4">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <span className="text-4xl">🐘</span>
          <div>
            <h1 className="text-2xl font-bold text-white">Tembo AI</h1>
            <p className="text-slate-400 text-sm">Your Kenya Travel Assistant</p>
          </div>
        </div>
      </header>

      {/* Chat Messages */}
      <main className="flex-1 overflow-y-auto px-4 py-6">
        <div className="max-w-4xl mx-auto space-y-4">
          {messages.length === 0 && (
            <div className="text-center py-12">
              <span className="text-6xl block mb-4">🇰🇪</span>
              <h2 className="text-2xl font-semibold text-white mb-2">Karibu! Welcome!</h2>
              <p className="text-slate-400 mb-6">Ask me anything about traveling in Kenya</p>
              <div className="flex flex-wrap justify-center gap-2">
                {['Masai Mara safari', 'Diani Beach', 'Amboseli elephants', 'Nairobi city'].map(suggestion => (
                  <button
                    key={suggestion}
                    onClick={() => setInput(`Tell me about ${suggestion}`)}
                    className="px-4 py-2 bg-slate-700/50 hover:bg-slate-700 text-slate-300 rounded-full text-sm transition-colors"
                  >
                    {suggestion}
                  </button>
                ))}
              </div>
            </div>
          )}

          {messages.map((message, index) => (
            <ChatMessage key={index} message={message} />
          ))}

          {isLoading && (
            <div className="flex items-start gap-3">
              <div className="w-10 h-10 rounded-full bg-emerald-600 flex items-center justify-center text-xl">
                🐘
              </div>
              <div className="bg-slate-700/50 rounded-2xl rounded-tl-sm px-4 py-3">
                <div className="flex gap-1">
                  <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></span>
                  <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></span>
                  <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></span>
                </div>
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </main>

      {/* Input Form */}
      <footer className="bg-slate-800/50 backdrop-blur-sm border-t border-slate-700 px-4 py-4">
        <form onSubmit={sendMessage} className="max-w-4xl mx-auto flex gap-3">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask about Kenya destinations, safaris, beaches..."
            className="flex-1 bg-slate-700 text-white placeholder-slate-400 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-all"
            disabled={isLoading}
          />
          <button
            type="submit"
            disabled={isLoading || !input.trim()}
            className="bg-emerald-600 hover:bg-emerald-500 disabled:bg-slate-600 disabled:cursor-not-allowed text-white px-6 py-3 rounded-xl font-medium transition-colors flex items-center gap-2"
          >
            <span>Send</span>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-5 h-5">
              <path d="M3.105 2.289a.75.75 0 00-.826.95l1.414 4.925A1.5 1.5 0 005.135 9.25h6.115a.75.75 0 010 1.5H5.135a1.5 1.5 0 00-1.442 1.086l-1.414 4.926a.75.75 0 00.826.95 28.896 28.896 0 0015.293-7.154.75.75 0 000-1.115A28.897 28.897 0 003.105 2.289z" />
            </svg>
          </button>
        </form>
      </footer>
    </div>
  )
}

function ChatMessage({ message }) {
  const isUser = message.role === 'user'

  return (
    <div className={`flex items-start gap-3 ${isUser ? 'flex-row-reverse' : ''} ${message.isTyping ? 'animate-fade-in' : ''}`}>
      {/* Avatar */}
      <div className={`w-10 h-10 rounded-full flex items-center justify-center text-xl flex-shrink-0 ${
        isUser ? 'bg-blue-600' : 'bg-emerald-600'
      }`}>
        {isUser ? '👤' : '🐘'}
      </div>

      {/* Message Content */}
      <div className={`max-w-[80%] ${isUser ? 'items-end' : 'items-start'}`}>
        <div className={`rounded-2xl px-4 py-3 ${
          isUser 
            ? 'bg-blue-600 text-white rounded-tr-sm' 
            : message.isError 
              ? 'bg-red-900/50 text-red-200 rounded-tl-sm'
              : 'bg-slate-700/50 text-slate-100 rounded-tl-sm'
        }`}>
          <p className="whitespace-pre-wrap">{message.content}</p>
        </div>

        {/* Sources */}
        {message.sources && message.sources.length > 0 && (
          <div className="mt-2 flex flex-wrap gap-1">
            {message.sources.slice(0, 3).map((source, i) => (
              <span key={i} className="text-xs bg-slate-700/30 text-slate-400 px-2 py-1 rounded">
                📍 {source.destination}
              </span>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

export default App
