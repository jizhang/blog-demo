import * as React from 'react'
import ListArrow from './ListArrow'
import ListSeparate from './ListSeparate'
import ListDataset from './ListDataset'

export default class Lists extends React.Component {
  state = {
    items: [
      { id: 1, text: 'Item 1' },
      { id: 2, text: 'Item 2' },
      ],
  }
  render() {
    return (
      <div style={{ lineHeight: '30px' }}>
        <h2>Example 3: List Items with Handlers</h2>

        <div style={{ cursor: 'pointer' }}>
          <h3>With arrow function:</h3>
          <ListArrow items={this.state.items} />
          <h3>With separate component:</h3>
          <ListSeparate items={this.state.items} />
          <h3>With HTML dataset:</h3>
          <ListDataset items={this.state.items} />
        </div>
      </div>
    )
  }
}
