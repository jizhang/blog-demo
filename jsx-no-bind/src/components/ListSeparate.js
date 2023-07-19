import * as React from 'react'

class Item extends React.PureComponent {
  handleClick = () => {
    this.props.onClick(this.props.item.id)
  }

  render() {
    return (
      <li onClick={this.handleClick}>{this.props.item.text}</li>
    )
  }
}

export default class ListSeparate extends React.Component {
  handleClick = (itemId) => {
    alert(itemId)
  }

  render() {
    return (
      <ul>
        {this.props.items.map(item => (
          <Item key={item.id} item={item} onClick={this.handleClick} />
        ))}
      </ul>
    )
  }
}
