import { useState, useRef, useEffect } from 'react'

const API_URL = 'http://localhost:8000'

// Typing effect hook
function useTypingEffect(text, speed = 20, enabled = true) {
  const [displayedText, setDisplayedText] = useState('')
  const [isComplete, setIsComplete] = useState(false)

  useEffect(() => {
    if (!enabled || !text) {
      setDisplayedText(text || '')
      setIsComplete(true)
      return
    }

    setDisplayedText('')
    setIsComplete(false)
    let i = 0
    const timer = setInterval(() => {
      if (i < text.length) {
        setDisplayedText(text.slice(0, i + 1))
        i++
      } else {
        setIsComplete(true)
        clearInterval(timer)
      }
    }, speed)

    return () => clearInterval(timer)
  }, [text, speed, enabled])

  return { displayedText, isComplete }
}

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [sessionId] = useState(() => `session_${Date.now()}`)
  const [category, setCategory] = useState('')
  const messagesEndRef = useRef(null)
  const inputRef = useRef(null)

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
    
    setMessages(prev => [...prev, { role: 'user', content: userMessage, timestamp: new Date() }])
    setIsLoading(true)

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userMessage,
          session_id: sessionId,
          category_filter: category || null
        })
      })

      if (!response.ok) throw new Error('Failed to get response')

      const data = await response.json()
      
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: data.answer,
        sources: data.sources,
        timestamp: new Date(),
        animate: true 
      }])

    } catch (error) {
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: 'Samahani! (Sorry) I encountered an error. Please try again.',
        isError: true,
        timestamp: new Date()
      }])
    } finally {
      setIsLoading(false)
      inputRef.current?.focus()
    }
  }

  const handleSuggestion = (text) => {
    setInput(text)
    inputRef.current?.focus()
  }

  const clearChat = () => {
    setMessages([])
  }

  const categories = [
    { value: '', label: 'All Topics', icon: '🌍' },
    { value: 'safari', label: 'Safari', icon: '🦁' },
    { value: 'beach', label: 'Beaches', icon: '🏖️' },
    { value: 'culture', label: 'Culture', icon: '🎭' },
    { value: 'transport', label: 'Transport', icon: '✈️' },
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-emerald-950 flex flex-col">
      {/* Animated Background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-amber-500/10 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }}></div>
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '2s' }}></div>
      </div>

      {/* Header */}
      <header className="relative z-10 bg-slate-900/80 backdrop-blur-xl border-b border-slate-700/50 px-4 py-4 shadow-xl">
        <div className="max-w-4xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="relative">
              <span className="text-5xl animate-bounce" style={{ animationDuration: '2s' }}>🐘</span>
              <span className="absolute -bottom-1 -right-1 text-lg">🇰🇪</span>
            </div>
            <div>
              <h1 className="text-2xl font-bold bg-gradient-to-r from-emerald-400 via-amber-400 to-red-500 bg-clip-text text-transparent">
                Tembo AI
              </h1>
              <p className="text-slate-400 text-sm flex items-center gap-2">
                <span className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></span>
                Kenya Travel Assistant
              </p>
            </div>
          </div>
          
          {messages.length > 0 && (
            <button
              onClick={clearChat}
              className="text-slate-400 hover:text-white text-sm flex items-center gap-1 px-3 py-1.5 rounded-lg hover:bg-slate-700/50 transition-all"
            >
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-4 h-4">
                <path fillRule="evenodd" d="M8.75 1A2.75 2.75 0 006 3.75v.443c-.795.077-1.584.176-2.365.298a.75.75 0 10.23 1.482l.149-.022.841 10.518A2.75 2.75 0 007.596 19h4.807a2.75 2.75 0 002.742-2.53l.841-10.519.149.023a.75.75 0 00.23-1.482A41.03 41.03 0 0014 3.193V3.75A2.75 2.75 0 0011.25 1h-2.5z" clipRule="evenodd" />
              </svg>
              Clear
            </button>
          )}
        </div>
      </header>

      {/* Chat Messages */}
      <main className="relative z-10 flex-1 overflow-y-auto px-4 py-6">
        <div className="max-w-4xl mx-auto space-y-6">
          {messages.length === 0 && (
            <div className="text-center py-8 animate-fade-in">
              {/* Hero Section */}
              <div className="relative inline-block mb-6">
                <span className="text-8xl block animate-float">🦁</span>
                <div className="absolute -inset-4 bg-gradient-to-r from-amber-500/20 to-emerald-500/20 rounded-full blur-2xl -z-10"></div>
              </div>
              
              <h2 className="text-3xl font-bold text-white mb-3">
                <span className="bg-gradient-to-r from-emerald-400 to-amber-400 bg-clip-text text-transparent">Karibu!</span> Welcome!
              </h2>
              <p className="text-slate-400 mb-8 text-lg">Discover the magic of Kenya — from savannas to shores</p>
              
              {/* Feature Cards */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-8">
                {[
                  { icon: '🦁', title: 'Safari', desc: 'Big Five & beyond' },
                  { icon: '🏖️', title: 'Beaches', desc: 'Pristine coastline' },
                  { icon: '⛰️', title: 'Mountains', desc: 'Mt. Kenya & more' },
                  { icon: '🏛️', title: 'Culture', desc: 'Rich heritage' },
                ].map((feature, i) => (
                  <div 
                    key={feature.title}
                    className="bg-slate-800/30 backdrop-blur-sm border border-slate-700/50 rounded-2xl p-4 hover:bg-slate-800/50 hover:border-emerald-500/30 transition-all hover:scale-105 cursor-pointer group"
                    style={{ animationDelay: `${i * 100}ms` }}
                    onClick={() => handleSuggestion(`Tell me about ${feature.title.toLowerCase()} in Kenya`)}
                  >
                    <span className="text-3xl mb-2 block group-hover:scale-110 transition-transform">{feature.icon}</span>
                    <h3 className="text-white font-semibold">{feature.title}</h3>
                    <p className="text-slate-500 text-xs">{feature.desc}</p>
                  </div>
                ))}
              </div>

              {/* Suggestion Chips */}
              <p className="text-slate-500 text-sm mb-3">Try asking about:</p>
              <div className="flex flex-wrap justify-center gap-2">
                {[
                  'Plan a safari to Masai Mara',
                  'Best beaches near Mombasa',
                  'Amboseli elephant watching',
                  'Budget travel tips Kenya',
                  'Wildebeest migration dates'
                ].map((suggestion, i) => (
                  <button
                    key={suggestion}
                    onClick={() => handleSuggestion(suggestion)}
                    className="px-4 py-2 bg-slate-800/50 hover:bg-emerald-600/20 border border-slate-700/50 hover:border-emerald-500/50 text-slate-300 hover:text-white rounded-full text-sm transition-all hover:scale-105"
                    style={{ animationDelay: `${i * 50}ms` }}
                  >
                    {suggestion}
                  </button>
                ))}
              </div>
            </div>
          )}

          {messages.map((message, index) => (
            <ChatMessage key={index} message={message} isLatest={index === messages.length - 1} />
          ))}

          {isLoading && <LoadingIndicator />}

          <div ref={messagesEndRef} />
        </div>
      </main>

      {/* Input Form */}
      <footer className="relative z-10 bg-slate-900/80 backdrop-blur-xl border-t border-slate-700/50 px-4 py-4">
        <div className="max-w-4xl mx-auto">
          {/* Category Filter */}
          <div className="flex gap-2 mb-3 overflow-x-auto pb-2 scrollbar-hide">
            {categories.map(cat => (
              <button
                key={cat.value}
                onClick={() => setCategory(cat.value)}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-sm whitespace-nowrap transition-all ${
                  category === cat.value
                    ? 'bg-emerald-600 text-white shadow-lg shadow-emerald-500/25'
                    : 'bg-slate-800/50 text-slate-400 hover:bg-slate-700/50 hover:text-white border border-slate-700/50'
                }`}
              >
                <span>{cat.icon}</span>
                <span>{cat.label}</span>
              </button>
            ))}
          </div>

          {/* Input */}
          <form onSubmit={sendMessage} className="flex gap-3">
            <div className="flex-1 relative">
              <input
                ref={inputRef}
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask about Kenya destinations, safaris, beaches..."
                className="w-full bg-slate-800/50 text-white placeholder-slate-500 rounded-2xl px-5 py-4 pr-12 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 border border-slate-700/50 focus:border-emerald-500/50 transition-all shadow-inner"
                disabled={isLoading}
              />
              <div className="absolute right-4 top-1/2 -translate-y-1/2 text-slate-600">
                <kbd className="text-xs bg-slate-700/50 px-1.5 py-0.5 rounded">⏎</kbd>
              </div>
            </div>
            <button
              type="submit"
              disabled={isLoading || !input.trim()}
              className="bg-gradient-to-r from-emerald-600 to-emerald-500 hover:from-emerald-500 hover:to-emerald-400 disabled:from-slate-700 disabled:to-slate-600 disabled:cursor-not-allowed text-white px-6 py-4 rounded-2xl font-medium transition-all flex items-center gap-2 shadow-lg shadow-emerald-500/25 disabled:shadow-none hover:scale-105 active:scale-95"
            >
              <span className="hidden sm:inline">Send</span>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-5 h-5">
                <path d="M3.105 2.289a.75.75 0 00-.826.95l1.414 4.925A1.5 1.5 0 005.135 9.25h6.115a.75.75 0 010 1.5H5.135a1.5 1.5 0 00-1.442 1.086l-1.414 4.926a.75.75 0 00.826.95 28.896 28.896 0 0015.293-7.154.75.75 0 000-1.115A28.897 28.897 0 003.105 2.289z" />
              </svg>
            </button>
          </form>

          {/* Footer Text */}
          <p className="text-center text-slate-600 text-xs mt-3">
            Powered by Groq AI • Local embeddings • 376+ Kenya travel docs
          </p>
        </div>
      </footer>
    </div>
  )
}

function ChatMessage({ message, isLatest }) {
  const isUser = message.role === 'user'
  const { displayedText, isComplete } = useTypingEffect(
    message.content, 
    15, 
    isLatest && message.animate && !isUser
  )

  const text = (isLatest && message.animate && !isUser) ? displayedText : message.content

  return (
    <div 
      className={`flex items-start gap-3 ${isUser ? 'flex-row-reverse' : ''} animate-slide-up`}
    >
      {/* Avatar */}
      <div className={`w-12 h-12 rounded-2xl flex items-center justify-center text-2xl flex-shrink-0 shadow-lg ${
        isUser 
          ? 'bg-gradient-to-br from-blue-500 to-blue-600 shadow-blue-500/25' 
          : 'bg-gradient-to-br from-emerald-500 to-emerald-600 shadow-emerald-500/25'
      }`}>
        {isUser ? '👤' : '🐘'}
      </div>

      {/* Message Content */}
      <div className={`max-w-[80%] ${isUser ? 'items-end' : 'items-start'}`}>
        {/* Name & Time */}
        <div className={`flex items-center gap-2 mb-1 ${isUser ? 'flex-row-reverse' : ''}`}>
          <span className="text-xs font-medium text-slate-400">
            {isUser ? 'You' : 'Tembo'}
          </span>
          <span className="text-xs text-slate-600">
            {message.timestamp?.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
          </span>
        </div>

        {/* Bubble */}
        <div className={`rounded-2xl px-5 py-4 shadow-xl ${
          isUser 
            ? 'bg-gradient-to-br from-blue-600 to-blue-700 text-white rounded-tr-sm shadow-blue-500/20' 
            : message.isError 
              ? 'bg-gradient-to-br from-red-900/80 to-red-800/80 text-red-100 rounded-tl-sm border border-red-700/50'
              : 'bg-gradient-to-br from-slate-800/90 to-slate-800/70 text-slate-100 rounded-tl-sm border border-slate-700/50 shadow-emerald-500/5'
        }`}>
          <p className="whitespace-pre-wrap leading-relaxed">{text}</p>
          {!isComplete && isLatest && message.animate && !isUser && (
            <span className="inline-block w-2 h-5 bg-emerald-400 ml-1 animate-pulse rounded-sm"></span>
          )}
        </div>

        {/* Sources */}
        {message.sources && message.sources.length > 0 && isComplete && (
          <div className="mt-3 flex flex-wrap gap-2 animate-fade-in">
            {message.sources.slice(0, 4).map((source, i) => (
              <span 
                key={i} 
                className="text-xs bg-slate-800/60 text-slate-400 px-3 py-1.5 rounded-full flex items-center gap-1.5 border border-slate-700/50 hover:border-emerald-500/30 transition-colors"
              >
                <span className="text-emerald-400">📍</span>
                {source.destination}
                <span className="text-slate-600">•</span>
                <span className="text-emerald-500/70">{Math.round(source.similarity * 100)}%</span>
              </span>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

function LoadingIndicator() {
  return (
    <div className="flex items-start gap-3 animate-slide-up">
      <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-emerald-500 to-emerald-600 flex items-center justify-center text-2xl shadow-lg shadow-emerald-500/25">
        🐘
      </div>
      <div className="bg-gradient-to-br from-slate-800/90 to-slate-800/70 rounded-2xl rounded-tl-sm px-5 py-4 border border-slate-700/50">
        <div className="flex items-center gap-3">
          <div className="flex gap-1.5">
            {[0, 1, 2].map(i => (
              <span 
                key={i}
                className="w-3 h-3 bg-emerald-500 rounded-full animate-bounce"
                style={{ animationDelay: `${i * 150}ms`, animationDuration: '0.8s' }}
              ></span>
            ))}
          </div>
          <span className="text-slate-500 text-sm">Tembo is thinking...</span>
        </div>
      </div>
    </div>
  )
}

export default App
