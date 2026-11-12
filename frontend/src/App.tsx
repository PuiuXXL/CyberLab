import { useState } from 'react'
import { getLabs, login } from './api/cyberlab'
import type { Lab, User } from './api/cyberlab'
import { LabCatalog } from './components/LabCatalog'
import { LoginScreen } from './components/LoginScreen'

type Catalog = { user: User; labs: Lab[] }

function App() {
  const [catalog, setCatalog] = useState<Catalog | null>(null)

  async function openCatalog(username: string) {
    const user = await login(username)
    const labs = await getLabs()
    setCatalog({ user, labs })
  }

  return catalog
    ? <LabCatalog user={catalog.user} labs={catalog.labs} />
    : <LoginScreen onLogin={openCatalog} />
}

export default App
