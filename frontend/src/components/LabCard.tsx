import type { Lab } from '../api/cyberlab'

const labTopics = new Map([
  ['SQL Injection', {
    kind: 'sql',
    sample: 'SELECT * FROM users',
    detail: 'WHERE id = ?',
  }],
  ['Cross-Site Scripting', {
    kind: 'xss',
    sample: '<script>',
    detail: '  runInBrowser()',
  }],
  ['Broken Access Control', {
    kind: 'access',
    sample: 'GET /admin',
    detail: '403 Forbidden',
  }],
])

export function LabCard({ lab }: { lab: Lab }) {
  const topic = labTopics.get(lab.name)

  return (
    <li className="lab-card" data-topic={topic?.kind}>
      {topic && (
        <div className="lab-card-visual" aria-hidden="true">
          <div className="lab-card-code">
            <code>{topic.sample}</code>
            <code>{topic.detail}</code>
          </div>
        </div>
      )}
      <div className="lab-card-body">
        {lab.category && <p className="lab-card-category">{lab.category}</p>}
        <h3>{lab.name}</h3>
        {lab.description && <p className="lab-card-description">{lab.description}</p>}
      </div>
    </li>
  )
}
