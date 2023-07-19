import * as React from 'react'

export default class ListDataset extends React.Component {
  handleClick = (event) => {
    alert(event.target.dataset.itemId)
  }

  render() {
    return (
      <ul>
        {this.props.items.map(item => (
          <li key={item.id} data-item-id={item.id} onClick={this.handleClick}>{item.text}</li>
        ))}
      </ul>
    )
  }
}
