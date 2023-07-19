import * as React from 'react'

export default class ListArrow extends React.Component {
  render() {
    return (
      <ul>
        {this.props.items.map(item => (
          <li key={item.id} onClick={() => { alert(item.id) }}>{item.text}</li>
        ))}
      </ul>
    )
  }
}
