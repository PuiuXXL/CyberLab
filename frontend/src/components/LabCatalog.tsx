import type { Lab, User } from '../api/cyberlab'
import { LabCard } from './LabCard'
import './LabCatalog.css'

type Props = {
  user: User
  labs: Lab[]
}

export function LabCatalog({ user, labs }: Props) {
  return (
    <div className="catalog-page">
      <header className="catalog-header">
        <div className="catalog-wrap catalog-header-inner">
          <span className="brand">Cyber <span>Lab</span></span>
          <span className="catalog-profile">
            <span className="catalog-avatar" aria-hidden="true">
              {Array.from(user.username)[0]?.toLocaleUpperCase('ro')}
            </span>
            <span>{user.username}</span>
          </span>
        </div>
      </header>
      <main className="catalog-wrap catalog">
        <div className="catalog-intro">
          <div className="catalog-intro-copy">
            <h1>Laboratoare</h1>
            <p>Explorează vulnerabilități web în medii de practică izolate.</p>
          </div>
          <div className="catalog-topology" aria-hidden="true">
            <span className="catalog-node catalog-node-client">Client</span>
            <span className="catalog-node catalog-node-app">Aplicație</span>
            <span className="catalog-node catalog-node-data">Date</span>
          </div>
        </div>

        <section className="catalog-library" aria-labelledby="catalog-library-title">
          <div className="catalog-library-heading">
            <h2 id="catalog-library-title">Catalog de practică</h2>
            <span>
              {labs.length} {labs.length === 1 ? 'laborator' : 'laboratoare'}
            </span>
          </div>
          {labs.length === 0 ? (
            <p className="catalog-empty">Momentan nu sunt laboratoare disponibile.</p>
          ) : (
            <ul className="lab-grid" role="list">
              {labs.map((lab) => <LabCard key={lab.id} lab={lab} />)}
            </ul>
          )}
        </section>
      </main>
    </div>
  )
}
