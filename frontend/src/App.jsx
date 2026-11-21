import { useEffect, useState } from 'react'

const API = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000'

const words = {
  en: {
    tag: 'Farming information, made easier',
    welcome: 'Your farm, your information hub',
    dashboard: 'Dashboard',
    advisory: 'Crop advisory',
    weather: 'Weather',
    market: 'Mandi prices',
    soil: 'Soil guide',
    profile: 'Farmer profile',
    name: 'Your name',
    state: 'State',
    district: 'District',
    language: 'Language',
    save: 'Save profile',
    crop: 'Crop name',
    question: 'What would you like to know?',
    ask: 'Get advice',
    ph: 'Soil pH (0–14)',
    check: 'Check soil note',
    loading: 'Loading…',
    disclaimer: 'Information support only. Confirm important decisions with your local agriculture officer / KVK.'
  },

  ta: {
    tag: 'விவசாயத் தகவல்கள் இனி எளிதாக',
    welcome: 'உங்கள் விவசாயத் தகவல் மையம்',
    dashboard: 'முகப்பு',
    advisory: 'பயிர் ஆலோசனை',
    weather: 'வானிலை',
    market: 'சந்தை விலை',
    soil: 'மண் வழிகாட்டி',
    profile: 'விவசாயி விவரம்',
    name: 'பெயர்',
    state: 'மாநிலம்',
    district: 'மாவட்டம்',
    language: 'மொழி',
    save: 'சேமிக்க',
    crop: 'பயிரின் பெயர்',
    question: 'உங்கள் கேள்வி என்ன?',
    ask: 'ஆலோசனை பெற',
    ph: 'மண் pH (0–14)',
    check: 'மண் தகவல் பார்க்க',
    loading: 'ஏற்றப்படுகிறது…',
    disclaimer: 'இது தகவல் உதவி மட்டுமே. முக்கிய முடிவுகளை உள்ளூர் வேளாண்மை அலுவலர் / KVK-யிடம் உறுதிப்படுத்தவும்.'
  },

  hi: {
    tag: 'खेती की जानकारी अब आसान',
    welcome: 'आपकी खेती की जानकारी का केंद्र',
    dashboard: 'डैशबोर्ड',
    advisory: 'फसल सलाह',
    weather: 'मौसम',
    market: 'मंडी भाव',
    soil: 'मिट्टी मार्गदर्शिका',
    profile: 'किसान प्रोफ़ाइल',
    name: 'आपका नाम',
    state: 'राज्य',
    district: 'ज़िला',
    language: 'भाषा',
    save: 'प्रोफ़ाइल सहेजें',
    crop: 'फसल का नाम',
    question: 'आप क्या जानना चाहते हैं?',
    ask: 'सलाह लें',
    ph: 'मिट्टी का pH (0–14)',
    check: 'मिट्टी जानकारी देखें',
    loading: 'लोड हो रहा है…',
    disclaimer: 'यह केवल सूचना सहायता है। महत्वपूर्ण निर्णय स्थानीय कृषि अधिकारी / KVK से सत्यापित करें।'
  }
}

const langNames = {
  en: 'English',
  ta: 'தமிழ்',
  hi: 'हिन्दी'
}

export default function App() {
  const [lang, setLang] = useState('en')
  const [page, setPage] = useState('dashboard')

  const [profile, setProfile] = useState({
    name: '',
    state: 'Tamil Nadu',
    district: '',
    language: 'en'
  })

  const [farmer, setFarmer] = useState(null)
  const [crop, setCrop] = useState('rice')
  const [question, setQuestion] = useState('')
  const [advice, setAdvice] = useState(null)
  const [weather, setWeather] = useState(null)
  const [mandi, setMandi] = useState(null)
  const [commodity, setCommodity] = useState('Tomato')
  const [ph, setPh] = useState('')
  const [soil, setSoil] = useState(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')

  const t = words[lang]

  useEffect(() => {
    setProfile(p => ({ ...p, language: lang }))
  }, [lang])

  async function api(path, options = {}) {
    const res = await fetch(API + path, {
      headers: { 'Content-Type': 'application/json' },
      ...options
    })

    const data = await res.json()

    if (!res.ok) {
      throw new Error(data.error || 'Request failed')
    }

    return data
  }

  async function saveProfile(e) {
    e.preventDefault()
    setError('')

    try {
      const p = await api('/api/farmers', {
        method: 'POST',
        body: JSON.stringify(profile)
      })

      setFarmer(p)
      setLang(p.language)
      setPage('dashboard')
    } catch (err) {
      setError(err.message)
    }
  }

  async function getAdvice(e) {
    e.preventDefault()
    setBusy(true)
    setError('')
    setAdvice(null)

    try {
      setAdvice(await api('/api/advisory', {
        method: 'POST',
        body: JSON.stringify({
          crop,
          question,
          language: lang
        })
      }))
    } catch (err) {
      setError(err.message + ' — Is the Flask backend running?')
    } finally {
      setBusy(false)
    }
  }

  async function loadWeather() {
    setBusy(true)
    setError('')

    try {
      setWeather(await api(
        '/api/weather?district=' + encodeURIComponent(profile.district)
      ))
    } catch (err) {
      setError(err.message + ' — Is the Flask backend running?')
    } finally {
      setBusy(false)
    }
  }

  async function loadMandi() {
    setBusy(true)
    setError('')
    setMandi(null)

    try {
      const data = await api(
        '/api/mandi?commodity=' + encodeURIComponent(commodity)
      )

      setMandi(data)
    } catch (err) {
      setError(err.message + ' — Is the Flask backend running?')
    } finally {
      setBusy(false)
    }
  }

  async function checkSoil(e) {
    e.preventDefault()
    setError('')

    try {
      setSoil(await api('/api/soil-advice', {
        method: 'POST',
        body: JSON.stringify({
          ph,
          language: lang
        })
      }))
    } catch (err) {
      setError(err.message)
    }
  }

  const nav = [
    ['dashboard', t.dashboard, '⌂'],
    ['advisory', t.advisory, '✳'],
    ['weather', t.weather, '☀'],
    ['market', t.market, '₹'],
    ['soil', t.soil, '♧'],
    ['profile', t.profile, '◉']
  ]

  return (
    <div className="app">

      <header className="topbar">
        <a
          className="brand"
          href="#"
          onClick={e => {
            e.preventDefault()
            setPage('dashboard')
          }}
        >
          <span className="brand-icon">🌱</span>
          <span>
            AgriSaathi
            <small>RESOURCE ADVISORY</small>
          </span>
        </a>

        <div className="top-actions">
          <span className="status-dot">●</span>

          <select
            aria-label="Language"
            value={lang}
            onChange={e => setLang(e.target.value)}
          >
            {Object.entries(langNames).map(([k, v]) => (
              <option key={k} value={k}>
                {v}
              </option>
            ))}
          </select>
        </div>
      </header>

      <div className="shell">

        <aside className="sidebar">
          <div className="side-label">MENU</div>

          {nav.map(([id, label, ico]) => (
            <button
              key={id}
              className={'nav-item ' + (page === id ? 'active' : '')}
              onClick={() => {
                setPage(id)
                setError('')
              }}
            >
              <span>{ico}</span>
              {label}
            </button>
          ))}

          <div className="side-note">
            <b>🌾 Farmer first</b>
            <p>
              Clear information for better-informed farming decisions.
            </p>
          </div>
        </aside>

        <main className="main">

          <div className="hero">
            <div>
              <div className="eyebrow">{t.tag}</div>
              <h1>{t.welcome}</h1>
              <p>Weather • Market • Soil • Crop guidance</p>
            </div>

            <div className="hero-art">🌾</div>
          </div>

          {error && (
            <div className="alert" role="alert">
              {error}
              <button onClick={() => setError('')}>×</button>
            </div>
          )}

          {page === 'dashboard' && (
            <>
              <div className="section-head">
                <div>
                  <h2>{t.dashboard}</h2>
                  <p className="muted">
                    A simple overview of your farm resources.
                  </p>
                </div>

                <span className="pill">● Prototype</span>
              </div>

              <div className="feature-grid">

                <button
                  className="feature-card green"
                  onClick={() => setPage('advisory')}
                >
                  <span className="feature-icon">🌱</span>
                  <b>{t.advisory}</b>
                  <small>Get crop-related information</small>
                  <span className="card-arrow">↗️</span>
                </button>

                <button
                  className="feature-card yellow"
                  onClick={() => {
                    setPage('weather')
                    loadWeather()
                  }}
                >
                  <span className="feature-icon">☀️</span>
                  <b>{t.weather}</b>
                  <small>Check weather information</small>
                  <span className="card-arrow">↗️</span>
                </button>

                <button
                  className="feature-card blue"
                  onClick={() => setPage('market')}
                >
                  <span className="feature-icon">📊</span>
                  <b>{t.market}</b>
                  <small>Find market data sources</small>
                  <span className="card-arrow">↗️</span>
                </button>

                <button
                  className="feature-card lilac"
                  onClick={() => setPage('soil')}
                >
                  <span className="feature-icon">🧪</span>
                  <b>{t.soil}</b>
                  <small>Understand a soil pH value</small>
                  <span className="card-arrow">↗️</span>
                </button>

              </div>

              <div className="panel welcome-panel">
                <div>
                  <span className="eyebrow">GET STARTED</span>

                  <h3>
                    {farmer
                      ? `Welcome, ${farmer.name}`
                      : 'Set up your farmer profile'}
                  </h3>

                  <p className="muted">
                    {farmer
                      ? `${farmer.district}, ${farmer.state}`
                      : 'Add your location to personalize the information shown in this prototype.'}
                  </p>
                </div>

                <button
                  className="primary"
                  onClick={() => setPage('profile')}
                >
                  {farmer ? 'Edit profile' : 'Create profile'} →
                </button>
              </div>
            </>
          )}

          {page === 'profile' && (
            <section className="panel form-panel">
              <h2>{t.profile}</h2>

              <p className="muted">
                Your location helps organize local information.
              </p>

              <form onSubmit={saveProfile} className="form-grid">

                <label>
                  {t.name}
                  <input
                    required
                    value={profile.name}
                    onChange={e =>
                      setProfile({ ...profile, name: e.target.value })
                    }
                    placeholder="Enter your name"
                  />
                </label>

                <label>
                  {t.state}
                  <input
                    required
                    value={profile.state}
                    onChange={e =>
                      setProfile({ ...profile, state: e.target.value })
                    }
                  />
                </label>

                <label>
                  {t.district}
                  <input
                    required
                    value={profile.district}
                    onChange={e =>
                      setProfile({ ...profile, district: e.target.value })
                    }
                    placeholder="e.g. Dharmapuri"
                  />
                </label>

                <label>
                  {t.language}
                  <select
                    value={profile.language}
                    onChange={e => {
                      setProfile({
                        ...profile,
                        language: e.target.value
                      })
                      setLang(e.target.value)
                    }}
                  >
                    {Object.entries(langNames).map(([k, v]) => (
                      <option value={k} key={k}>
                        {v}
                      </option>
                    ))}
                  </select>
                </label>

                <button className="primary" type="submit">
                  {t.save}
                </button>

              </form>
            </section>
          )}

          {page === 'advisory' && (
            <section className="panel form-panel">
              <span className="eyebrow">CROP SUPPORT</span>

              <h2>{t.advisory}</h2>

              <p className="muted">
                Ask a question about your crop. The current version uses a
                small transparent rule-based example, not a trained AI model.
              </p>

              <form onSubmit={getAdvice}>

                <label>
                  {t.crop}
                  <select
                    value={crop}
                    onChange={e => setCrop(e.target.value)}
                  >
                    <option value="rice">Rice / நெல் / धान</option>
                    <option value="tomato">Tomato / தக்காளி / टमाटर</option>
                    <option value="groundnut">
                      Groundnut / நிலக்கடலை / मूँगफली
                    </option>
                    <option value="other">Other crop</option>
                  </select>
                </label>

                <label>
                  {t.question}
                  <textarea
                    value={question}
                    onChange={e => setQuestion(e.target.value)}
                    placeholder="Describe your crop or issue…"
                  />
                </label>

                <div className="button-row">
                  <button className="primary" disabled={busy}>
                    {busy ? t.loading : t.ask}
                  </button>
                </div>

              </form>

              {advice && (
                <div className="result">
                  <div className="result-title">
                    <h3>{advice.title}</h3>
                  </div>

                  <p>{advice.answer}</p>
                  <p className="note">{advice.note}</p>
                  <small>Method: {advice.method}</small>
                </div>
              )}
            </section>
          )}

          {page === 'weather' && (
            <section className="panel">
              <span className="eyebrow">LOCAL CONDITIONS</span>

              <h2>{t.weather}</h2>

              <p className="muted">
                District: {profile.district || 'Not set'}
              </p>

              <button
                className="primary"
                onClick={loadWeather}
                disabled={busy}
              >
                {busy ? t.loading : 'Load weather information'}
              </button>

              {weather && (
                <div className="result">
                  <h3>{weather.district}</h3>
                  <p>{weather.summary}</p>
                  <p className="note">Source: {weather.source}</p>
                  <small>
                    Updated: {new Date(weather.updated_at).toLocaleString()}
                  </small>
                </div>
              )}
            </section>
          )}

          {page === 'market' && (
            <section className="panel form-panel">
              <span className="eyebrow">
                ALL INDIA MARKET INFORMATION
              </span>

              <h2>{t.market}</h2>

              <label>
                Commodity
                <input
                  value={commodity}
                  onChange={e => setCommodity(e.target.value)}
                  placeholder="e.g. Tomato, Onion, Paddy"
                />
              </label>

              <p className="muted">
                Search mandi prices across India.
              </p>

              <button
                className="primary"
                onClick={loadMandi}
                disabled={busy}
              >
                {busy ? t.loading : 'Get Mandi Prices'}
              </button>

              {mandi && (
                <>
                  <div className="result">
                    <h3>{mandi.commodity} — India</h3>
                    <p>{mandi.message}</p>
                    <p className="note">Source: {mandi.source}</p>
                  </div>

                  {mandi.prices?.length > 0 ? (
                    <div style={{ overflowX: 'auto', marginTop: '18px' }}>
                      <table
                        style={{
                          width: '100%',
                          borderCollapse: 'collapse',
                          textAlign: 'left'
                        }}
                      >
                        <thead>
                          <tr>
                            {[
                              'Market',
                              'District',
                              'State',
                              'Min ₹',
                              'Max ₹',
                              'Modal ₹',
                              'Date'
                            ].map(x => (
                              <th
                                key={x}
                                style={{
                                  padding: '10px',
                                  borderBottom: '1px solid #ddd'
                                }}
                              >
                                {x}
                              </th>
                            ))}
                          </tr>
                        </thead>

                        <tbody>
                          {mandi.prices.map((item, index) => (
                            <tr key={index}>
                              <td style={{ padding: '10px', borderBottom: '1px solid #eee' }}>
                                {item.market || '-'}
                              </td>
                              <td style={{ padding: '10px', borderBottom: '1px solid #eee' }}>
                                {item.district || '-'}
                              </td>
                              <td style={{ padding: '10px', borderBottom: '1px solid #eee' }}>
                                {item.state || '-'}
                              </td>
                              <td style={{ padding: '10px', borderBottom: '1px solid #eee' }}>
                                ₹{item.min_price ?? '-'}
                              </td>
                              <td style={{ padding: '10px', borderBottom: '1px solid #eee' }}>
                                ₹{item.max_price ?? '-'}
                              </td>
                              <td style={{ padding: '10px', borderBottom: '1px solid #eee' }}>
                                ₹{item.modal_price ?? '-'}
                              </td>
                              <td style={{ padding: '10px', borderBottom: '1px solid #eee' }}>
                                {item.date || '-'}
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  ) : (
                    <p className="note">
                      No price records returned. Try another commodity.
                    </p>
                  )}
                </>
              )}
            </section>
          )}

          {page === 'soil' && (
            <section className="panel form-panel">
              <span className="eyebrow">SOIL HEALTH</span>

              <h2>{t.soil}</h2>

              <p className="muted">
                Enter the pH value from a soil test report.
              </p>

              <form onSubmit={checkSoil}>
                <label>
                  {t.ph}
                  <input
                    type="number"
                    min="0"
                    max="14"
                    step="0.1"
                    required
                    value={ph}
                    onChange={e => setPh(e.target.value)}
                    placeholder="e.g. 6.5"
                  />
                </label>

                <button className="primary">
                  {t.check}
                </button>
              </form>

              {soil && (
                <div className="result">
                  <h3>Soil pH: {soil.ph}</h3>
                  <p>{soil.message}</p>
                  <small>Source: {soil.source}</small>
                </div>
              )}
            </section>
          )}

          <footer>
            {t.disclaimer}
            <div>
              Built as a multilingual agricultural information prototype.
            </div>
          </footer>

        </main>
      </div>
    </div>
  )
}